---
meta:
  state: massachusetts
  abbreviation: MA
  last_verified: 2026-01-06
  complexity: high
  has_medical_schools: true
  has_public_schools: true
  # Matches index: md: 1/1, do: 0/0
  md_preference_total: 1   # UMass Chan only (others are private)
  md_preference_public: 1
  do_preference_total: 0   # UNECOM is private with no state preference
  do_preference_public: 0

# Massachusetts uses 7-YEAR residency rule for classification
admissions_residency:
  type: domicile_based
  determination_by: school  # UMass Chan determines via Residency Validation form
  required_years: 7
  consecutive: true
  school_counts: false

family_derivation:
  enabled: true
  eligible_relationships:
    - parent
    - spouse
    - child
    - sibling  # Siblings count for family derivation
  required_duration_years: 7

schools:
  # MD Schools with preference
  - name: UMass T.H. Chan School of Medicine
    degree: MD
    type: public
    application_system: AMCAS
    class_size: 142
    resident_percentage: 70  # Updated: ~70% MA residents
    nonresident_percentage: 30
    secondary_process: prescreened  # Not all applicants receive secondary
    secondary_focus:
      - "Diversity contribution"
      - "Competencies (leadership, teamwork, empathy, communication, inquiry)"
      - "Why UMass Chan"
      - "Health equity experience"
    citizenship:
      eligible:
        - us_citizen
        - permanent_resident
        - canadian_citizen
        - canadian_permanent_resident
        - daca
        - refugee
        - asylee
      ineligible:
        - f1_visa
        - j1_visa
        - other_nonimmigrant
    notes:
      - "F-1/J-1 CANNOT APPLY - citizenship requirement for admission"
      - "MD-PhD has no residency requirement"
      - "Pre-screens applicants before sending secondaries"
      - "Rolling admissions - interviews Sept through March"

  # Private MD schools - no residency preference (listed for reference)
  - name: Harvard Medical School
    degree: MD
    type: private
    application_system: AMCAS
    residency_preference: none
  - name: Boston University Chobanian & Avedisian School of Medicine
    degree: MD
    type: private
    application_system: AMCAS
    residency_preference: none
  - name: Tufts University School of Medicine
    degree: MD
    type: private
    application_system: AMCAS
    residency_preference: none

citizenship:
  admission_citizenship_required: true  # F-1/J-1 cannot apply to UMass Chan
  eligible:
    - us_citizen
    - permanent_resident
    - canadian_citizen
    - canadian_permanent_resident
    - daca
    - refugee
    - asylee
  ineligible:
    - f1_visa
    - j1_visa
    - other_nonimmigrant

military:
  notes:
    - "Federal Section 702 applies for GI Bill users"
    - "Contact UMass Chan directly for current military policies"

special_programs:
  - name: MD-PhD Program
    residency_required: false
    notes: "Out-of-state applicants evaluated equally for MD-PhD"

documentation:
  primary:
    - federal_tax_returns_7_years
    - massachusetts_tax_returns_7_years
  supporting:
    - employment_proof
    - deed_or_lease
    - mortgage_rent_utility
    - drivers_license
---

# Massachusetts Medical School Admissions Residency

**Last Verified**: 2026-01-06

## Sources Index

| ID | Source | URL |
|----|--------|-----|
| [1] | UMass Chan Residency Classification | https://www.umassmed.edu/som/admissions/apply/massachusetts-residency-classification/ |
| [2] | UMass Chan FAQs | https://www.umassmed.edu/som/admissions/faqs/ |
| [3] | Massachusetts General Laws Chapter 75 Section 34A | https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXII/Chapter75/Section34A |
| [4] | UMass Chan Class Profile | https://www.umassmed.edu/som/student-community/class-profiles/ |

---

## Admissions Classification System

Massachusetts requires **7 CONSECUTIVE YEARS** of residency for classification.

### Legal Basis — [3]

Massachusetts General Laws Chapter 75, Section 34A defines residency:

> "a resident shall be deemed to be a person who has **resided in the Commonwealth for 7 consecutive years or more** prior to enrollment or a person whose **immediate family has resided in the Commonwealth for 7 consecutive years or more** prior to his enrollment."

### How You're Classified — [1]

UMass Chan classifies applicants via the **Residency Validation (RV) form** in the secondary application. This determines whether you're in the Massachusetts resident or non-resident applicant pool.

---

## Two Pathways to Resident Classification — [1][3]

### Pathway 1: Personal Residency
- **You** have lived in Massachusetts for 7+ consecutive years prior to enrollment
- Must be domicile (permanent home), not just presence for school

### Pathway 2: Family Residency
- Your **immediate family member** has 7+ years MA domicile
- **Immediate family**: Parent, spouse, child, or **sibling**
- You don't need to have lived in MA yourself

**Example**: If your sibling has lived in MA for 8 years, you qualify as a MA resident even if you've never lived there.

---

## Class Composition — [4]

| Classification | Percentage |
|----------------|------------|
| Massachusetts Resident | 64% |
| Non-Resident | 36% |

**Note**: UMass Chan officially states both residents and non-residents are "eligible to apply" and are "considered" — but the class composition shows strong preference for MA residents.

---

## Citizenship Requirements — [2]

### Can Apply to UMass Chan

| Status | Eligible? |
|--------|-----------|
| US Citizens | YES |
| US Permanent Residents | YES |
| Canadian Citizens | YES |
| Canadian Permanent Residents | YES |
| DACA Recipients | YES |
| Refugees | YES |
| Asylees | YES |

### Cannot Apply to UMass Chan

| Status | Eligible? |
|--------|-----------|
| **F-1 Visa (Student)** | **NO** |
| **J-1 Visa (Exchange)** | **NO** |
| **Other Nonimmigrant Visas** | **NO** |

**F-1/J-1 visa holders cannot apply** to UMass Chan School of Medicine.

---

## Documentation Requirements — [1]

### Primary Evidence (Required)
- **7 years of uninterrupted Federal AND Massachusetts tax returns**
- Tax returns must list Massachusetts as legal residence (not P.O. Box)
- If dependent: Parent/guardian tax returns showing MA residence

### Supporting Documentation
- Employment proof in Massachusetts
- Deed or lease agreements
- Mortgage/rent/utility receipts
- Valid Massachusetts driver's license

### Burden of Proof — [1]
- Rests on the applicant
- Each case decided on its own merits
- "No single indicium is decisive"

---

## School Attendance Does NOT Count — [1]

**CRITICAL WARNING**:

"Attendance at a Massachusetts university or college does not, by itself, establish Massachusetts residency during that timeframe." — [1]

**Example**: 4 years of undergrad at a MA school does NOT count toward the 7-year requirement.

---

## MD-PhD Exception — [2]

**Important for out-of-state applicants**:

"Massachusetts residency is NOT required for application to the MD-PhD Program." — [2]

MD-PhD applicants are evaluated regardless of state of residence.

---

## Common Scenarios

### Scenario 1: 4 Years Undergrad in MA
- **Situation**: Attended Boston College for undergrad, now applying to UMass Chan
- **Classification**: NON-RESIDENT (school doesn't count, only 4 years anyway)

### Scenario 2: Parents in MA for 10 Years
- **Situation**: Parents in MA 10 years, you went to college out of state
- **Classification**: RESIDENT (parents' 7+ years qualifies you)

### Scenario 3: Sibling in MA for 8 Years
- **Situation**: Your sibling has lived in MA for 8 years, you've never lived there
- **Classification**: RESIDENT (sibling qualifies as immediate family)

### Scenario 4: F-1 Visa Student
- **Situation**: International student on F-1 visa
- **Classification**: CANNOT APPLY to UMass Chan (citizenship requirement)

---

## Key Takeaways

1. **7 years required** - Virtually impossible to establish from scratch before applying
2. **Family pathway is the key** - If parent, spouse, child, or sibling has 7+ years, you qualify
3. **Sibling counts** - Can qualify through brother/sister's 7-year residency
4. **F-1/J-1 cannot apply** - Citizenship requirement for admission to UMass Chan
5. **College doesn't count** - School attendance doesn't establish residency
6. **64% of class is in-state** - Strong practical preference despite "no formal preference" policy
7. **MD-PhD is the exception** - No residency requirement for combined program
