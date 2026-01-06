# Front Matter Schema

This document defines the YAML front matter structure for state research files.

**Design Principle**: This schema defines **structure and types**, not values. State-specific data belongs in state files. Adding a new state should NEVER require editing this schema.

---

## Scope: Admissions Classification Only

This schema focuses on **admissions residency** - how applicants are classified as resident/nonresident for admission purposes. This affects:
- Which applicant pool you compete in
- Seat reservations (e.g., 90% resident requirements)
- Acceptance rate differential

**Programs covered**: Both MD (allopathic) and DO (osteopathic) medical schools.

**Application systems**:
- **AMCAS** - MD programs (except Texas)
- **AACOMAS** - DO programs
- **TMDSAS** - Texas MD and DO programs

**NOT covered**: Tuition classification (what you pay after admission).

---

## File Structure Overview

Each `policies/states/{state}.md` file has:
1. YAML front matter (structured data)
2. Markdown body (prose, sources, citations)

**Related files:**
- `index.yaml` - Compact routing index, flag definitions (always loaded)
- `regional_programs/*.yaml` - Centralized regional program data

---

## Required Fields

### meta

```yaml
meta:
  state: string              # Full state name (lowercase)
  abbreviation: string       # Two-letter code
  last_verified: date        # YYYY-MM-DD format
  complexity: enum           # low | medium | high | very_high
  has_medical_schools: boolean
  has_public_schools: boolean

  # School counts - MUST match index.yaml
  md_preference_total: integer   # MD schools with residency-based admission preference
  md_preference_public: integer  # Public subset
  do_preference_total: integer   # DO schools with residency-based admission preference
  do_preference_public: integer  # Public subset
```

**Complexity levels:**
- `low` - Simple rules, few exceptions
- `medium` - Standard rules with some nuance
- `high` - Complex rules or multiple pathways
- `very_high` - Highly complex, many exceptions, or unique systems

### admissions_residency

```yaml
admissions_residency:
  type: enum                 # state_level | school_specific | domicile_based | ties_screening | hybrid
  determination_by: string   # Who determines: "state" | "school" | system name
  centralized_system: string # Optional: system name if centralized (e.g., "TMDSAS")

  # Duration requirement - use ONE format (at top level or nested)
  required_days: integer
  required_months: integer
  required_years: integer
  school_counts: boolean     # Does educational presence count?
  continuous: boolean        # Must be continuous?

  # OR nested structure for complex rules
  physical_presence:
    required_days: integer
    required_months: integer
    school_counts: boolean
    continuous: boolean
    credit_limit: integer    # Max credits while establishing (optional)
    deadline: string         # When requirement must be met

  # Multiple pathways (when state has alternate routes)
  pathways:
    - type: string           # e.g., "high_school_graduation", "domicile_establishment"
      requirements: object   # State-specific requirement details
```

### schools

```yaml
schools:
  - name: string             # Full school name
    degree: enum             # MD | DO
    type: enum               # public | private | state_assisted
    application_system: enum # AMCAS | AACOMAS | TMDSAS (recommended)

    # Optional fields
    class_size: integer
    resident_percentage: integer
    instate_percentage: integer

    # Per-school citizenship (when differs from state default)
    citizenship:
      eligible: string[]
      ineligible: string[]
      notes: string[]

    # Per-school preferences (tiered)
    preferences:
      - tier: integer
        criteria: string
        states: string[]     # For regional preferences
```

### citizenship

State-level defaults (can be overridden per-school):

```yaml
citizenship:
  eligible: string[]         # List of eligible statuses
  ineligible: string[]       # List of ineligible statuses
  admission_citizenship_required: boolean  # true = must be citizen/PR to apply
  notes: string[]            # Optional explanatory notes
```

**Common citizenship categories:**
- `us_citizen`, `permanent_resident`
- `daca`, `daca_ab540`, `undocumented`
- `refugee`, `asylee`
- `canadian_citizen`, `canadian_permanent_resident`
- `cofa_citizen`
- `f1_visa`, `j1_visa`, `h1b_visa`, `tn_visa`, `other_nonimmigrant`
- `international`

### military

```yaml
military:
  active_duty_exempt: boolean
  spouse_included: boolean
  dependents_included: boolean
  veteran_va_benefits_exempt: boolean
  national_guard_exempt: boolean   # Optional
  notes: string[]                  # Optional
```

---

## Optional Sections

Include only when a state has the relevant feature.

### financial_independence

```yaml
financial_independence:
  grad_students_presumed_independent: boolean
  dependent_inherits_parent: boolean
  can_establish_own_while_dependent: boolean
```

### marriage_transfer

Used when marriage can transfer residency status.

```yaml
marriage_transfer:
  enabled: boolean
  spouse_domicile_required_months: integer
  marriage_duration_required_months: integer
```

### ties_screening

Used when classification is criteria-based rather than duration-based.

```yaml
ties_screening:
  enabled: boolean
  criteria: string[]           # List of criteria names
  minimum_required: integer    # How many criteria must be met
  equivalent_regions:
    enabled: boolean
    regions: string[]          # Regions treated as equivalent (defined in state file)
```

### family_derivation

Used when extended family can establish eligibility.

```yaml
family_derivation:
  enabled: boolean
  eligible_relationships: string[]  # e.g., [parent, spouse, sibling]
  required_duration_years: integer
```

### service_obligation

Used when there's a mandatory or optional practice commitment.

```yaml
service_obligation:
  required: boolean            # true = mandatory, false = optional program
  years: integer
  location: string             # Where service must be performed
  alternative: string          # e.g., "repay_plus_interest"
  penalty_interest_rate: number
```

### regional_program

Used for states in regional programs (WWAMI, SREB, etc.).

```yaml
regional_program:
  name: string                 # Reference to regional_programs/*.yaml
  role: enum                   # lead | member
  member_states: string[]
  certification_required: boolean
  certification_deadline: string
  seats_per_year: integer
```

### special_programs

Used for state-specific programs (tuition waivers, pathway programs).

```yaml
special_programs:
  - name: string
    type: string               # tuition_waiver, pathway, etc.
    eligibility: string
    benefit: string
    obligation: string
```

### deadlines

```yaml
deadlines:
  application: string
  residency_certification: string
  mcat_latest: string
```

### intent

Used when states require documented intent to establish residency.

```yaml
intent:
  timing: string             # When intent must be established
  required_docs: string[]    # Required documentation
  supporting_docs: string[]  # Additional supporting documents
  relinquish_other_state_license: boolean  # Must give up other state docs
```

### nonresident_cap

Used when state law caps non-resident admissions.

```yaml
nonresident_cap:
  percentage: integer        # Max % of class that can be non-resident
  enforced_by: string        # "law" | "policy"
  note: string               # Optional explanation
```

### documentation

Used to specify what documentation is required for residency verification.

```yaml
documentation:
  primary: string[]          # Required documents
  supporting: string[]       # Optional supporting documents
```

---

## Index.yaml Format

The `index.yaml` uses a compressed format for scalability (<3K tokens for 52 jurisdictions).

### State Entry Format

```yaml
states:
  {state_key}:
    abbr: string              # Two-letter abbreviation
    dur: string               # Duration: Nd | Nm | Ny (days/months/years)
    md: string                # "total/public" for MD schools with preference
    do: string                # "total/public" for DO schools with preference
    cx: enum                  # l | m | h | vh
    f: string[]               # Flags from index.yaml → flags:
    prg: string[]             # Regional programs: [wwami], [sreb], []
    sys: string               # Optional: centralized system name
    note: string              # Optional: key feature
```

### Pending State Format

```yaml
{state_key}: {abbr: XX, status: pending}
{state_key}: {abbr: XX, prg: [program], status: pending}
```

---

## Enum Reference

### complexity
`low` | `medium` | `high` | `very_high`

### admissions_residency.type
- `state_level` - All schools follow state rules
- `school_specific` - Each school has own rules
- `domicile_based` - Duration-based domicile requirement
- `ties_screening` - Subjective criteria-based
- `hybrid` - Mix of systems

### schools[].degree
`MD` | `DO`

### schools[].type
`public` | `private` | `state_assisted`

### schools[].application_system
`AMCAS` | `AACOMAS` | `TMDSAS`

### regional_program.role
`lead` | `member`

---

## Validation Rules

### When Adding/Updating States

1. **Index ↔ State File Sync**
   - `md: X/Y` in index must match `md_preference_total: X, md_preference_public: Y`
   - `do: X/Y` must match similarly
   - Every school counted must have a `schools:` entry

2. **School Entry Requirements**
   - **REQUIRED**: `name`, `degree`, `type`
   - **RECOMMENDED**: `application_system`
   - **CONDITIONAL**: `citizenship` if differs from state default

3. **Flag Usage**
   - Only use flags defined in `index.yaml` → `flags:`
   - Add new flag definitions to index.yaml first

4. **Regional Programs**
   - If `prg: [program]`, include `regional_program:` section
   - Member state lists must match across files

5. **Documentation Independence**
   - No cross-state comparisons ("longest in US", "unlike California")
   - State facts directly without superlatives
   - Internal comparisons (within state) are acceptable

---

## State File Template

```yaml
---
meta:
  state: {state_name}
  abbreviation: {XX}
  last_verified: {YYYY-MM-DD}
  complexity: {level}
  has_medical_schools: {boolean}
  has_public_schools: {boolean}
  md_preference_total: {N}
  md_preference_public: {N}
  do_preference_total: {N}
  do_preference_public: {N}

admissions_residency:
  type: {type}
  determination_by: {who}
  required_months: {N}

schools:
  - name: "{School Name}"
    degree: {MD|DO}
    type: {type}
    application_system: {system}

citizenship:
  eligible: [us_citizen, permanent_resident]
  ineligible: [f1_visa, j1_visa]

military:
  active_duty_exempt: true
  spouse_included: true
---

# {State} Medical School Admissions Residency

**Last Verified**: {YYYY-MM-DD}

## Sources Index

| ID | Source | URL |
|----|--------|-----|
| [1] | {Source Name} | {URL} |

---

{Content with inline citations [1]}
```
