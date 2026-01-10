#!/usr/bin/env python3
"""
Policy Validation Script

Validates state YAML files against schema and reports inconsistencies.
Run with: python scripts/validate-policies.py
"""

import os
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("Error: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)


# Paths relative to project root
PROJECT_ROOT = Path(__file__).parent.parent
POLICIES_DIR = PROJECT_ROOT / "policies"
SCHEMA_DIR = POLICIES_DIR / "schema"
INDEX_PATH = POLICIES_DIR / "index.yaml"
STATES_DIR = POLICIES_DIR / "states"
CLAUDE_MD_PATH = PROJECT_ROOT / ".claude" / "CLAUDE.md"


class ValidationResult:
    def __init__(self):
        self.errors: list[dict] = []
        self.warnings: list[dict] = []

    def add_error(self, file: str, message: str, field: str = None):
        self.errors.append({"file": file, "message": message, "field": field})

    def add_warning(self, file: str, message: str, field: str = None):
        self.warnings.append({"file": file, "message": message, "field": field})


def load_yaml(path: Path) -> dict:
    """Load a YAML file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_text(path: Path) -> str:
    """Load a text file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_schema() -> dict:
    """Load schema from policies/schema/ directory."""
    if not SCHEMA_DIR.exists():
        raise FileNotFoundError(f"Schema directory not found: {SCHEMA_DIR}")

    schema = {}
    schema_files = ["core.yaml", "schools.yaml", "optional.yaml", "enums.yaml", "validation.yaml"]
    for filename in schema_files:
        filepath = SCHEMA_DIR / filename
        if filepath.exists():
            schema.update(load_yaml(filepath))
    return schema


def extract_schema_info(schema: dict) -> dict:
    """Extract field definitions, enums, and required sections from schema."""
    info = {
        "required_sections": ["meta", "sources", "rules_for_determining_residency_status", "schools"],
        "optional_sections": [],
        "enums": {},
        "documented_fields": set(),
        "school_fields": set(),
    }

    # Extract enums from split schema (enums are top-level keys from enums.yaml)
    enum_keys = {
        "complexity": "complexity",
        "residency_type": "residency_type",
        "entity_determines": "entity_determines",
        "degree": "degree",
        "school_type": "school_type",
        "application_system": "application_system",
        "geographic_preference": "geographic_preference",
        "secondary_handling": "secondary_handling",
        "regional_role": "regional_role",
    }

    for enum_name, schema_key in enum_keys.items():
        if schema_key in schema and "values" in schema[schema_key]:
            info["enums"][enum_name] = schema[schema_key]["values"]

    # Extract citizenship values from enums.yaml
    if "citizenship_status" in schema and "values" in schema["citizenship_status"]:
        info["citizenship_values"] = set(schema["citizenship_status"]["values"])
    else:
        info["citizenship_values"] = set()

    # Extract optional sections
    optional_markers = [
        "rules_for_dependent_vs_independent_students",
        "rules_for_transferring_residency_via_marriage",
        "criteria_used_for_residency_classification",
        "rules_for_deriving_residency_from_family",
        "required_service_after_graduation",
        "programs_with_special_eligibility_rules",
        "legal_limit_on_nonresident_admissions",
        "documents_required_for_residency_verification",
        "eligible_citizenship_and_immigration_statuses",
        "military_residency_exemptions_and_benefits",
        "questions_requiring_further_research",
    ]
    info["optional_sections"] = optional_markers

    # Extract documented school-level fields
    try:
        school_fields = schema["schools"]["item_fields"]
        info["school_fields"] = set(school_fields.keys())
    except (KeyError, TypeError):
        pass

    # Build set of all documented top-level fields
    info["documented_fields"] = set(info["required_sections"]) | set(info["optional_sections"])

    return info


def get_all_keys_recursive(obj: Any, prefix: str = "") -> set[str]:
    """Recursively get all keys from a nested dict structure."""
    keys = set()
    if isinstance(obj, dict):
        for key, value in obj.items():
            full_key = f"{prefix}.{key}" if prefix else key
            keys.add(full_key)
            keys.update(get_all_keys_recursive(value, full_key))
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            keys.update(get_all_keys_recursive(item, prefix))
    return keys


def validate_type_conditional_fields(state: dict, rel_path: str, results: ValidationResult):
    """Validate fields based on rules_for_determining_residency_status.type.

    Different residency types have different required/forbidden fields:
    - domicile_based: REQUIRES months_of_residency_required, school_time_counts_toward_residency
    - ties_screening: Should NOT have duration fields at state level
    - school_specific: Schools define their own rules via school_specific_residency_rules
    - hybrid: Similar to domicile_based but also needs ties criteria
    """
    rules = state.get("rules_for_determining_residency_status", {})
    res_type = rules.get("type")

    if not res_type:
        return

    if res_type == "domicile_based":
        # Requires duration fields
        if "months_of_residency_required" not in rules:
            results.add_error(str(rel_path), "type=domicile_based requires 'months_of_residency_required' field", "rules_for_determining_residency_status")
        if "school_time_counts_toward_residency" not in rules:
            results.add_warning(str(rel_path), "type=domicile_based should have 'school_time_counts_toward_residency' field", "rules_for_determining_residency_status")

    elif res_type == "ties_screening":
        # Should NOT have duration fields (ties-based doesn't use duration)
        if "months_of_residency_required" in rules:
            results.add_warning(str(rel_path), "type=ties_screening typically doesn't use 'months_of_residency_required' (ties-based, not duration-based)", "rules_for_determining_residency_status")

    elif res_type == "school_specific":
        # Schools define their own rules via school_specific_residency_rules
        # (per_school_residency_summary was deprecated - schools array is sufficient)
        pass

    elif res_type == "hybrid":
        # Combines duration AND ties - needs both
        if "months_of_residency_required" not in rules:
            results.add_warning(str(rel_path), "type=hybrid typically needs 'months_of_residency_required' (combines duration and ties)", "rules_for_determining_residency_status")


def validate_citizenship_values(state: dict, valid_values: set, rel_path: str, results: ValidationResult):
    """Validate citizenship statuses against schema's common_values list.

    Warns when a citizenship status used in eligible/ineligible arrays
    isn't in the schema's documented common_values.
    """
    def check_values(obj: any, path: str):
        if isinstance(obj, dict):
            # Check eligible and ineligible arrays
            for field in ["eligible", "ineligible"]:
                if field in obj and isinstance(obj[field], list):
                    for value in obj[field]:
                        if isinstance(value, str) and value not in valid_values:
                            results.add_warning(str(rel_path), f"Undocumented citizenship status: '{value}' (add to schema common_values if intentional)", f"{path}.{field}")
            # Recurse into nested dicts
            for key, value in obj.items():
                check_values(value, f"{path}.{key}" if path else key)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                check_values(item, path)

    # Check state-level citizenship
    if "eligible_citizenship_and_immigration_statuses" in state:
        check_values(state["eligible_citizenship_and_immigration_statuses"], "eligible_citizenship_and_immigration_statuses")

    # Check school-level citizenship
    if "schools" in state:
        for i, school in enumerate(state["schools"]):
            if "citizenship" in school:
                check_values(school["citizenship"], f"schools[{i}].citizenship")


def validate_source_sequentiality(sources: list, rel_path: str, results: ValidationResult):
    """Validate that source IDs are sequential starting at 1."""
    if not sources:
        return

    source_ids = []
    for s in sources:
        if isinstance(s, dict) and "id" in s:
            source_ids.append(s["id"])

    if not source_ids:
        return

    # Check starts at 1
    if source_ids[0] != 1:
        results.add_warning(str(rel_path), f"Source IDs should start at 1, but first ID is {source_ids[0]}", "sources")

    # Check sequential (no gaps)
    expected = 1
    for sid in sorted(source_ids):
        if sid != expected:
            results.add_warning(str(rel_path), f"Source IDs have gaps: expected {expected}, found {sid}", "sources")
            break
        expected += 1


def validate_tiered_priorities(school: dict, school_prefix: str, rel_path: str, results: ValidationResult):
    """Validate tiered_priorities_for_admission has sequential tiers starting at 1."""
    tiers = school.get("tiered_priorities_for_admission", [])
    if not tiers:
        return

    tier_nums = []
    for t in tiers:
        if isinstance(t, dict) and "tier" in t:
            tier_nums.append(t["tier"])

    if not tier_nums:
        return

    # Check starts at 1
    if min(tier_nums) != 1:
        results.add_warning(str(rel_path), f"Tiers should start at 1, but minimum tier is {min(tier_nums)}", f"{school_prefix}.tiered_priorities_for_admission")

    # Check sequential
    tier_nums_sorted = sorted(tier_nums)
    for i, tier in enumerate(tier_nums_sorted, start=1):
        if tier != i:
            results.add_warning(str(rel_path), f"Tier numbers not sequential: expected {i}, found {tier}", f"{school_prefix}.tiered_priorities_for_admission")
            break


def validate_regional_program_consistency(state: dict, rel_path: str, results: ValidationResult):
    """Validate regional program role consistency.

    - If state has participation_in_regional_program.role: lead → should have member_states
    - If school has role_in_regional_program: lead → should have seats_allocated_by_campus_location
    """
    # State-level check
    participation = state.get("participation_in_regional_program", {})
    if isinstance(participation, dict):
        if participation.get("role") == "lead":
            if "member_states" not in participation:
                results.add_warning(str(rel_path), "participation_in_regional_program.role=lead should have 'member_states' array", "participation_in_regional_program")

    # School-level: role_in_regional_program=lead
    # Note: seats_allocated_by_campus_location lives in regional_programs/*.yaml (SSOT)
    # No validation needed here - regional program files are the source of truth


def validate_state_file(state_path: Path, schema_info: dict, index: dict, results: ValidationResult):
    """Validate a single state file."""
    rel_path = state_path.relative_to(PROJECT_ROOT)
    state_name = state_path.stem

    try:
        state = load_yaml(state_path)
    except Exception as e:
        results.add_error(str(rel_path), f"Failed to parse YAML: {e}")
        return

    if not state:
        results.add_error(str(rel_path), "File is empty or invalid")
        return

    # Check required sections
    for section in schema_info["required_sections"]:
        if section not in state:
            results.add_error(str(rel_path), f"Missing required section: {section}")

    # Run new bulk validations
    validate_type_conditional_fields(state, rel_path, results)
    validate_citizenship_values(state, schema_info["citizenship_values"], rel_path, results)
    validate_source_sequentiality(state.get("sources", []), rel_path, results)
    validate_regional_program_consistency(state, rel_path, results)

    # Check for undocumented top-level sections
    all_known_sections = schema_info["documented_fields"]
    for section in state.keys():
        if section not in all_known_sections:
            results.add_warning(str(rel_path), f"Undocumented top-level section: {section}", section)

    # Validate meta.complexity enum
    if "meta" in state and "complexity" in state.get("meta", {}):
        complexity = state["meta"]["complexity"]
        valid_values = schema_info["enums"].get("complexity", [])
        if valid_values and complexity not in valid_values:
            results.add_error(str(rel_path), f"Invalid complexity value: {complexity} (valid: {valid_values})", "meta.complexity")

    # Validate rules_for_determining_residency_status
    if "rules_for_determining_residency_status" in state:
        rules = state["rules_for_determining_residency_status"]

        # Validate type enum
        if "type" in rules:
            valid_types = schema_info["enums"].get("residency_type", [])
            if valid_types and rules["type"] not in valid_types:
                results.add_error(str(rel_path), f"Invalid residency type: {rules['type']} (valid: {valid_types})", "rules_for_determining_residency_status.type")

        # Validate entity_that_determines_residency_status enum
        if "entity_that_determines_residency_status" in rules:
            valid_entities = schema_info["enums"].get("entity_determines", [])
            if valid_entities and rules["entity_that_determines_residency_status"] not in valid_entities:
                results.add_warning(str(rel_path), f"Undocumented entity: {rules['entity_that_determines_residency_status']} (known: {valid_entities})", "rules_for_determining_residency_status.entity_that_determines_residency_status")

        # Validate date format (should be lowercase_month_day like june_22)
        if "date_residency_must_be_established_by" in rules:
            date_val = rules["date_residency_must_be_established_by"]
            if not re.match(r'^[a-z]+_\d{1,2}$', str(date_val)):
                results.add_warning(str(rel_path), f"Date format should be lowercase_month_day (e.g., june_22), got: {date_val}", "rules_for_determining_residency_status.date_residency_must_be_established_by")

        # Conditional: ties_screening requires criteria_used_for_residency_classification
        if rules.get("type") == "ties_screening":
            if "criteria_used_for_residency_classification" not in state:
                results.add_warning(str(rel_path), "type=ties_screening but missing criteria_used_for_residency_classification section")

    # Regional program info lives in regional_programs/*.yaml (SSOT)
    # State files should NOT have participation_in_regional_program section
    # The index.yaml prg: field routes to the regional program file

    # Validate schools array
    if "schools" in state:
        for i, school in enumerate(state["schools"]):
            school_prefix = f"schools[{i}]"

            # Check required school fields
            if "name" not in school:
                results.add_error(str(rel_path), f"{school_prefix}: Missing required field 'name'")
            if "degree" not in school:
                results.add_error(str(rel_path), f"{school_prefix}: Missing required field 'degree'")
            if "type" not in school:
                results.add_error(str(rel_path), f"{school_prefix}: Missing required field 'type'")

            # Validate degree enum
            if "degree" in school:
                valid_degrees = schema_info["enums"].get("degree", [])
                if valid_degrees and school["degree"] not in valid_degrees:
                    results.add_error(str(rel_path), f"{school_prefix}: Invalid degree: {school['degree']}", f"{school_prefix}.degree")

            # Validate type enum
            if "type" in school:
                valid_types = schema_info["enums"].get("school_type", [])
                if valid_types and school["type"] not in valid_types:
                    results.add_error(str(rel_path), f"{school_prefix}: Invalid type: {school['type']}", f"{school_prefix}.type")

            # Validate application_system enum
            if "application_system" in school:
                valid_systems = schema_info["enums"].get("application_system", [])
                if valid_systems and school["application_system"] not in valid_systems:
                    results.add_error(str(rel_path), f"{school_prefix}: Invalid application_system: {school['application_system']}", f"{school_prefix}.application_system")

            # Validate geographic_area_giving_admission_preference enum
            if "geographic_area_giving_admission_preference" in school:
                valid_prefs = schema_info["enums"].get("geographic_preference", [])
                pref = school["geographic_area_giving_admission_preference"]
                if valid_prefs and pref not in valid_prefs:
                    results.add_warning(str(rel_path), f"{school_prefix}: Undocumented geographic preference: {pref}", f"{school_prefix}.geographic_area_giving_admission_preference")

            # Check for undocumented school fields
            for field in school.keys():
                if field not in schema_info["school_fields"]:
                    results.add_warning(str(rel_path), f"{school_prefix}: Undocumented school field: {field}", f"{school_prefix}.{field}")

            # Validate role_in_regional_program enum
            if "role_in_regional_program" in school:
                valid_roles = schema_info["enums"].get("regional_role", [])
                if valid_roles and school["role_in_regional_program"] not in valid_roles:
                    results.add_warning(str(rel_path), f"{school_prefix}: Invalid role_in_regional_program: {school['role_in_regional_program']}", f"{school_prefix}.role_in_regional_program")

            # Validate school-specific date formats in routes_to_qualify_for_school
            if "routes_to_qualify_for_school" in school:
                for j, route in enumerate(school["routes_to_qualify_for_school"]):
                    if isinstance(route, dict) and "deadline" in route:
                        deadline = route["deadline"]
                        if not re.match(r'^[a-z]+_\d{1,2}$', str(deadline)):
                            results.add_warning(str(rel_path), f"{school_prefix}.routes_to_qualify_for_school[{j}]: Date format should be lowercase_month_day, got: {deadline}")

            # Validate school_specific_residency_rules deadline format
            if "school_specific_residency_rules" in school:
                rules = school["school_specific_residency_rules"]
                if isinstance(rules, dict) and "deadline" in rules:
                    deadline = rules["deadline"]
                    if not re.match(r'^[a-z]+_\d{1,2}$', str(deadline)):
                        results.add_warning(str(rel_path), f"{school_prefix}.school_specific_residency_rules.deadline: Date format should be lowercase_month_day, got: {deadline}")

            # Validate citizenship blocks have both eligible and ineligible
            if "citizenship" in school:
                cit = school["citizenship"]
                if "eligible" not in cit:
                    results.add_error(str(rel_path), f"{school_prefix}.citizenship: Missing 'eligible' array")
                if "ineligible" not in cit:
                    results.add_error(str(rel_path), f"{school_prefix}.citizenship: Missing 'ineligible' array")

            # Validate tiered priorities structure
            validate_tiered_priorities(school, school_prefix, rel_path, results)

    # Validate state-level citizenship
    if "eligible_citizenship_and_immigration_statuses" in state:
        cit = state["eligible_citizenship_and_immigration_statuses"]
        if isinstance(cit, dict):
            # Allow per_school_citizenship_summary as alternative when schools differ
            has_summary = "per_school_citizenship_summary" in cit
            if "eligible" not in cit and not has_summary:
                results.add_warning(str(rel_path), "eligible_citizenship_and_immigration_statuses: Missing 'eligible' array (or use per_school_citizenship_summary when schools differ)")
            if "ineligible" not in cit and not has_summary:
                results.add_warning(str(rel_path), "eligible_citizenship_and_immigration_statuses: Missing 'ineligible' array (or use per_school_citizenship_summary when schools differ)")

    # Validate school counts against index
    # NOTE: Index counts schools WITH residency preference, state files list ALL schools.
    # A mismatch is normal when some schools don't give preference (e.g., private schools).
    if state_name in index.get("states", {}):
        index_entry = index["states"][state_name]

        # Skip pending states
        if index_entry.get("status") == "pending":
            return

        schools = state.get("schools", [])

        # Check MD count - warning only since index counts preference schools
        if "md" in index_entry:
            md_str = index_entry["md"]
            if "/" in str(md_str):
                total_md = int(str(md_str).split("/")[0])
                actual_md = len([s for s in schools if s.get("degree") == "MD"])
                if actual_md < total_md:
                    results.add_error(str(rel_path), f"MD school count: index expects {total_md} with preference, file has only {actual_md}")
                elif actual_md > total_md:
                    # More schools than index is expected (some without preference)
                    results.add_warning(str(rel_path), f"MD school count: index says {total_md} with preference, file has {actual_md} total (OK if extras lack preference)")

        # Check DO count - warning only since index counts preference schools
        if "do" in index_entry:
            do_str = index_entry["do"]
            if "/" in str(do_str):
                total_do = int(str(do_str).split("/")[0])
                actual_do = len([s for s in schools if s.get("degree") == "DO"])
                if actual_do < total_do:
                    results.add_error(str(rel_path), f"DO school count: index expects {total_do} with preference, file has only {actual_do}")
                elif actual_do > total_do:
                    # More schools than index is expected (some without preference)
                    results.add_warning(str(rel_path), f"DO school count: index says {total_do} with preference, file has {actual_do} total (OK if extras lack preference)")

    # Validate source references
    if "sources" in state:
        source_ids = {s.get("id") for s in state["sources"] if isinstance(s, dict)}

        # Check all source references in the file
        def check_source_refs(obj, path=""):
            if isinstance(obj, dict):
                if "sources" in obj and obj["sources"] != state["sources"]:
                    refs = obj["sources"]
                    if isinstance(refs, list):
                        for ref in refs:
                            if isinstance(ref, int) and ref not in source_ids:
                                results.add_warning(str(rel_path), f"Reference to undefined source ID: {ref}", path)
                for key, value in obj.items():
                    check_source_refs(value, f"{path}.{key}" if path else key)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    check_source_refs(item, path)

        check_source_refs(state)


def validate_index(index: dict, results: ValidationResult):
    """Validate index.yaml internal consistency."""
    rel_path = "policies/index.yaml"

    # Check that defined flags are used
    defined_flags = set(index.get("flags", {}).keys())

    for state_name, state_data in index.get("states", {}).items():
        if isinstance(state_data, dict) and "f" in state_data:
            for flag in state_data["f"]:
                if flag not in defined_flags:
                    results.add_error(rel_path, f"State '{state_name}' uses undefined flag: {flag}")

    # Check stats match actual counts
    states = index.get("states", {})
    researched = sum(1 for s in states.values() if isinstance(s, dict) and s.get("status") != "pending")
    pending = sum(1 for s in states.values() if isinstance(s, dict) and s.get("status") == "pending")

    stats = index.get("stats", {})
    if stats.get("researched") != researched:
        results.add_warning(rel_path, f"stats.researched ({stats.get('researched')}) doesn't match actual count ({researched})")
    if stats.get("pending") != pending:
        results.add_warning(rel_path, f"stats.pending ({stats.get('pending')}) doesn't match actual count ({pending})")


def validate_claude_md(claude_md: str, results: ValidationResult):
    """Check CLAUDE.md for section names that don't match schema."""
    rel_path = ".claude/CLAUDE.md"

    # Known mismatches between what CLAUDE.md might say and what schema uses
    wrong_to_right = {
        "admissions_residency:": "rules_for_determining_residency_status:",
        "citizenship:": "eligible_citizenship_and_immigration_statuses:",
        "military:": "military_residency_exemptions_and_benefits:",
        "research_gaps:": "questions_requiring_further_research:",
    }

    for wrong, right in wrong_to_right.items():
        # Look for the wrong term in a context that suggests it's a section name
        # (in code blocks or bullet points describing file structure)
        if wrong in claude_md:
            # Check if it's in a context describing file sections
            pattern = rf"[-`]\s*{re.escape(wrong)}"
            if re.search(pattern, claude_md):
                results.add_error(rel_path, f"References '{wrong}' but schema uses '{right}'")


def format_report(results: ValidationResult) -> str:
    """Format validation results as markdown."""
    lines = ["# Policy Validation Report", ""]

    # Summary
    lines.append("## Summary")
    lines.append(f"- Errors: {len(results.errors)}")
    lines.append(f"- Warnings: {len(results.warnings)}")
    lines.append("")

    if not results.errors and not results.warnings:
        lines.append("All validations passed!")
        return "\n".join(lines)

    # Errors grouped by file
    if results.errors:
        lines.append("## Errors (must fix)")
        lines.append("")

        errors_by_file: dict[str, list] = {}
        for err in results.errors:
            errors_by_file.setdefault(err["file"], []).append(err)

        for file, errs in sorted(errors_by_file.items()):
            lines.append(f"### {file}")
            for err in errs:
                if err["field"]:
                    lines.append(f"- {err['message']}")
                    lines.append(f"  - Field: `{err['field']}`")
                else:
                    lines.append(f"- {err['message']}")
            lines.append("")

    # Warnings grouped by file
    if results.warnings:
        lines.append("## Warnings (should fix)")
        lines.append("")

        warnings_by_file: dict[str, list] = {}
        for warn in results.warnings:
            warnings_by_file.setdefault(warn["file"], []).append(warn)

        for file, warns in sorted(warnings_by_file.items()):
            lines.append(f"### {file}")
            for warn in warns:
                if warn["field"]:
                    lines.append(f"- {warn['message']}")
                    lines.append(f"  - Field: `{warn['field']}`")
                else:
                    lines.append(f"- {warn['message']}")
            lines.append("")

    # How to fix
    lines.append("## How to Fix")
    lines.append("")
    lines.append("1. **Undocumented fields**: Add to schema/ or remove from state file")
    lines.append("2. **Invalid enum values**: Use value from schema or add to enums.yaml")
    lines.append("3. **Count mismatches**: Update index.yaml or state file schools array")
    lines.append("4. **Cross-reference issues**: Update CLAUDE.md to match schema")
    lines.append("5. **Missing arrays**: Add both `eligible: []` and `ineligible: []` to citizenship blocks")

    return "\n".join(lines)


def main():
    results = ValidationResult()

    # Load core files
    try:
        schema = load_schema()
        index = load_yaml(INDEX_PATH)
        claude_md = load_text(CLAUDE_MD_PATH) if CLAUDE_MD_PATH.exists() else ""
    except Exception as e:
        print(f"Error loading core files: {e}")
        sys.exit(1)

    # Extract schema info
    schema_info = extract_schema_info(schema)

    # Validate index.yaml
    validate_index(index, results)

    # Validate CLAUDE.md cross-references
    if claude_md:
        validate_claude_md(claude_md, results)

    # Validate each state file
    if STATES_DIR.exists():
        for state_file in sorted(STATES_DIR.glob("*.yaml")):
            validate_state_file(state_file, schema_info, index, results)

    # Output report
    report = format_report(results)
    print(report)

    # Exit with error code if validation failed
    sys.exit(1 if results.errors else 0)


if __name__ == "__main__":
    main()
