# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

AI agent helping medical school applicants understand **admissions residency** - which applicant pool they compete in and which schools give them an admission advantage.

**Scope**:
- **Programs**: Both MD (allopathic) and DO (osteopathic) medical schools
- **Focus**: Admissions classification only (not tuition residency)

**Application Systems**:
- **AMCAS** - MD programs (except Texas)
- **AACOMAS** - DO programs
- **TMDSAS** - Texas MD and DO programs

## Project Structure

```
policies/
├── index.yaml                    # Compact routing index (always loaded, <3K tokens)
├── schema.md                     # Documents front matter schema
├── states/
│   └── {state}.md                # YAML front matter + markdown body
└── regional_programs/
    ├── wwami.yaml                # Washington-Wyoming-Alaska-Montana-Idaho (MD)
    └── sreb.yaml                 # Southern Regional Education Board (DO reserved seats)
```

### Coverage Status

See `policies/index.yaml` → `stats:` for current coverage.

---

## Single Source of Truth (SSOT) Principle

Each piece of information lives in exactly one place. Do not duplicate content across files.

| Information | Source of Truth | Other Files Should |
|-------------|-----------------|-------------------|
| Flag definitions | `index.yaml` → `flags:` | Reference, not copy |
| State data | `index.yaml` → `states:` | Reference, not copy |
| Statistics | `index.yaml` → `stats:` | Reference, not copy |
| Schema/format | `schema.md` | Reference, not copy |
| State policies | `states/{state}.md` | Not duplicated elsewhere |
| Regional programs | `regional_programs/*.yaml` | Not duplicated elsewhere |

**Why**: Prevents drift. When updating data, update ONE file. All references stay in sync.

---

## Ripple Effect Analysis (MANDATORY)

**After ANY edit to files in this project, you MUST analyze ripple effects before considering the task complete.**

### Trigger Conditions

Perform ripple analysis after:
- Editing ANY `.yaml` or `.md` file in `policies/`
- Adding or removing fields from any file
- Changing statistics, counts, or enumerations
- Modifying schema or flag definitions

### Analysis Checklist

1. **Cross-references**: Does any other file reference what I just changed?
   - `index.yaml` → referenced by CLAUDE.md, schema.md, state files
   - `schema.md` → defines structure used by all state files
   - Flag definitions → used across all state entries
   - Statistics → must match actual file counts

2. **Terminology consistency**: Did I use a term that appears elsewhere?
   - Check if the same term/value exists in other files
   - Ensure consistent naming (e.g., "states" vs "jurisdictions")

3. **Schema compliance**: If I edited a state file, does it still match schema.md?
   - Are all sections I used documented in the schema?
   - If I added a new section type, did I add it to schema.md?

4. **Comments and documentation**: Do comments still reflect reality?
   - YAML comments (`# like this`) can become stale
   - Inline notes in markdown body

### How To Check

```
Files to cross-reference after edits:
├── index.yaml        ← stats, flags, state entries
├── schema.md         ← field definitions, enums, validation rules
├── CLAUDE.md         ← references to other files, process docs
├── states/*.md       ← must comply with schema, match index counts
└── regional_programs/*.yaml ← member lists must match index
```

**If you find inconsistencies, fix them in the same session.** Do not leave the project in an inconsistent state.

---

## Schema & Format Documentation

**See `policies/schema.md`** for complete schema documentation including:
- Field definitions and validation rules
- Format examples for state files
- Enum values for all fields

**See `policies/index.yaml`** for:
- Flag definitions (the authoritative source)
- Current state data
- Regional program references

---

## Validation Checklist

When adding or updating state files, verify:

1. **Counts match**: `md: X/Y` in index ↔ `md_preference_total/public` in state file
2. **Schools documented**: Every school counted in index has a `schools:` entry with `degree` field
3. **Flags defined**: Only use flags from `index.yaml` → `flags:`
4. **Regional programs**: If `prg: [wwami]`, include `regional_program:` section

**See `policies/schema.md` → Validation Rules** for complete validation requirements.

---

## Research Workflow

Research produces verified claims. Every claim traces to a source read in this conversation.

**The process:**
1. **Read** - Visit the source (WebFetch, browser, Read tool)
2. **Document** - Record what you see: "This page shows: [content]"
3. **Write** - State claims based only on documented content
4. **Cite** - Link claim to the source you just read

Research output follows research input. No exceptions.

---

## Source Standards

### Authority Hierarchy
1. Medical school admissions pages (primary)
2. State medical education boards
3. State legislature / statutes
4. University system policies

### Domain Requirement
Medical school research requires medical school sources. General university or undergraduate sources don't apply.

### Accessibility Requirement
Only cite sources you can access and verify. If a source is paywalled, restricted, or inaccessible, note "not publicly verifiable" rather than citing it.

---

## Research Completeness

For every policy or program, document:
- **Who** qualifies
- **How** to apply (and when in the process)
- **When** deadlines apply
- **What** benefits or obligations result

Distinguish clearly:
- Admission eligibility vs tuition eligibility
- State-level vs school-specific policies
- Dependent vs independent student rules

---

## Output Format

### Citation Format
Sources Index table in markdown body, inline citations throughout:

```markdown
| ID | Source | URL |
|----|--------|-----|
| [1] | School Admissions | https://... |

"Claim here" — [1]
```

### Data Model
- **Layer 1: State Residency** - Legal determination of which state(s) you qualify for
- **Layer 2: School Preferences** - Advantages beyond residency (regional programs, ties criteria)

### Documentation Independence
Each state file must be **self-contained** without cross-state comparisons.

**Do NOT write:**
- "unlike Massachusetts" or "compared to California"
- "unique to this state" or "different from most states"
- Tables comparing this state to other states

**DO write:**
- State the fact directly: "7 years required" not "7 years (longest in the US)"
- Internal comparisons within a state are acceptable: "Unlike UW Medicine, WSU ESFCOM requires..."
- Comparing student types within a state is acceptable: "Unlike undergrads, grad students are presumed independent"

**Why:** Each file should be readable independently. The agent compares states; the documentation describes each state's rules.

---

## Agent Behavior

- Track all potentially relevant states
- Identify weak residency claims proactively
- Cite specific statute/policy sections
- Provide strengthening advice for borderline cases

### How Agent Loads Data

1. **Always load**: `index.yaml` (<3K tokens) - routes to candidate states via flags
2. **Selective load**: `{state}.md` front matter (~500 tokens each) - structured data for 2-5 candidates
3. **On demand**: `{state}.md` body (~3K tokens) - citations, deep questions, edge cases
4. **If needed**: `regional_programs/*.yaml` - for WWAMI, SREB questions

### Token Budget Per Query

| Component | Tokens | When |
|-----------|--------|------|
| Index | ~2,500 | Always |
| Front matters (3-5 states) | ~1,500-2,500 | Per query |
| Full body (1-2 states) | ~3,000-6,000 | Deep questions |
| Regional program | ~500 | If relevant |
| **Total** | **~8,000-11,000** | Typical query |

---

## Research Priority

When adding new states, prioritize by applicant impact.

See `policies/index.yaml` → `research_priority` for the full prioritized list.
