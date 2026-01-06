---
meta:
  state: hawaii
  abbreviation: HI
  last_verified: 2026-01-06
  complexity: high
  has_medical_schools: true
  has_public_schools: true
  # Matches index: md: 1/1, do: 0/0
  md_preference_total: 1   # JABSOM only
  md_preference_public: 1
  do_preference_total: 0   # No DO schools in Hawaii
  do_preference_public: 0

# Hawaii uses TIES SCREENING for admissions classification
# Subjective criteria-based system (not based on days of residency)
admissions_residency:
  type: ties_screening  # Subjective, criteria-based
  determination_by: school  # JABSOM determines, not state

ties_screening:
  criteria:
    - applicant_legal_residence
    - parent_legal_residence
    - birthplace
    - high_school_location
    - college_location
  minimum_required: 2  # Must meet at least 2 of 5 criteria
  pacific_islands_equivalent: true
  pacific_islands:
    - american_samoa
    - cnmi
    - cook_islands
    - fsm
    - futuna
    - guam
    - kiribati
    - nauru
    - niue
    - rapa_nui
    - palau
    - marshall_islands
    - solomon_islands
    - tokelau
    - tonga
    - tuvalu
    - vanuatu
    - wallis

schools:
  - name: John A. Burns School of Medicine (JABSOM)
    degree: MD
    type: public
    application_system: AMCAS
    class_size: 77
    resident_seats: 67
    nonresident_seats: 10
    resident_percentage: 87
    secondary_focus:
      - "Background and lived experiences contributing to JABSOM mission"
      - "Community contribution"
      - "Hawaii/Pacific connection" # KEY - explain ties or why applying without ties
    citizenship:
      eligible:
        - us_citizen
        - permanent_resident
        - daca
        - undocumented
        - cofa_citizen
        - f1_visa  # Can apply - no citizenship requirement
        - j1_visa  # Can apply
        - international  # JABSOM accepts regardless of country of origin
      notes:
        - "No citizenship requirement for admission"
        - "Accepts applicants without regard to country of origin"
        - "90 semester credits at US/Canadian institution required"
        - "Pacific Islanders considered part of same group as Native Hawaiians for scholarships/programs"

citizenship:
  # State-level defaults (JABSOM is more permissive)
  eligible:
    - us_citizen
    - permanent_resident
    - daca
    - undocumented
    - cofa_citizen
  admission_citizenship_required: false  # JABSOM accepts international

military:
  active_duty_resident: true
  spouse_included: true
  dependents_included: true
  national_guard_resident: true
  reserves_hawaii_based_resident: true
---

# Hawaii Medical School Admissions Residency

**Last Verified**: 2026-01-06

## Sources Index

| ID | Source | URL |
|----|--------|-----|
| [1] | JABSOM Residency Screening | https://admissions.jabsom.hawaii.edu/application-process/residency-screening.html |
| [2] | JABSOM FAQs | https://admissions.jabsom.hawaii.edu/faqs/ |
| [3] | JABSOM Incoming Class Profile | https://admissions.jabsom.hawaii.edu/application-process/2025-incoming-class-profile.html |

---

## Admissions Classification: Ties Screening

**Hawaii uses a SUBJECTIVE ties-based screening system** to classify applicants as "resident" or "nonresident" for admissions purposes. Classification is based on meeting 2 of 5 criteria rather than days of physical presence.

### The Five Criteria — [1]

JABSOM evaluates applicants on FIVE criteria:

1. **Applicant's legal residence** (current state of residence)
2. **Parents' legal residence** (where parents currently live)
3. **Birthplace** (where applicant was born)
4. **High school location** (where applicant attended high school)
5. **College/university location** (where applicant attended undergrad)

### Classification Rule — [1]

| Criteria Met | Classification |
|--------------|----------------|
| 2 or more | **Resident** for admissions |
| Fewer than 2 | **Nonresident** for admissions |

### Pacific Islands Equivalent — [1]

Ties to the following Pacific Island nations/territories count THE SAME as Hawaii ties:

- American Samoa
- Commonwealth of the Northern Mariana Islands (CNMI)
- Cook Islands
- Federated States of Micronesia (FSM)
- Guam
- Kiribati
- Nauru
- Niue
- Rapa Nui (Easter Island)
- Republic of Palau
- Republic of the Marshall Islands
- Solomon Islands
- Tokelau
- Tonga
- Tuvalu
- Vanuatu
- Wallis & Futuna

**Example**: Applicant born in Guam (Pacific Island birthplace = 1 criterion) who attended high school in Hawaii (2nd criterion) = RESIDENT for admissions.

---

## Class Composition — [1][3]

| Category | Seats | Percentage |
|----------|-------|------------|
| Resident | ~67 | 87% |
| Nonresident | ~10 | 13% |
| **Total** | **77** | 100% |

JABSOM's mission prioritizes training physicians for Hawaii and the Pacific. Nonresident candidates must be "highly ranked, preferably with some ties to Hawaii" to be accepted. — [1]

---

## Citizenship Requirements for Admission — [2]

### JABSOM is Citizenship-Blind for Admission

**"Applicants are considered for admission to JABSOM without regard to their country of origin."** — [2]

This means:
- **International students CAN apply**
- **F-1 visa holders CAN apply**
- **DACA recipients CAN apply**
- **Undocumented students CAN apply**

**Requirements regardless of citizenship:**
- Complete 90 semester credits at a US or Canadian institution — [2]
- Meet all other admissions requirements

### Citizenship Affects Seat Pool, Not Eligibility

An F-1 visa holder or international student who meets 2+ ties criteria (e.g., born in Pacific Islands, attended Hawaii high school) would be classified as **"resident for admissions"** and compete for the 67 resident seats rather than the 10 nonresident seats. — [1]

---

## Military Classification — [1]

The following receive **resident classification for admissions**:

- Active duty military stationed in Hawaii
- Spouses and dependents of active duty in Hawaii
- Hawaii National Guard members
- Hawaii-based Reserve unit members

---

## How Ties Are Verified — [1]

Information is pulled from:
1. **AMCAS application** (primary application)
2. **JABSOM secondary application**

The secondary application includes an essay where applicants can explain their ties to Hawaii or Pacific Islands.

---

## Secondary Application Focus

The key secondary essay asks about your **Hawaii/Pacific connection**. If you don't have a personal connection, you must explain why you're applying.

### Pacific Island Applicants

If you are from the Pacific Islands (not specifically Hawaiian), JABSOM considers you part of the broader Pacific Islander community and treats your ties equivalently to Hawaii ties.

---

## Common Scenarios

### Scenario 1: Born in Hawaii, Left as Child
- **Birthplace**: Hawaii (1 criterion) ✓
- **Need**: At least 1 more criterion (parents still in HI? HS in HI?)
- **If only 1 criterion**: Classified as NONRESIDENT for admissions — [1]

### Scenario 2: From Guam, College on Mainland
- **Birthplace**: Guam (Pacific Island = 1 criterion) ✓
- **Parents' residence**: Guam (if applicable = 2nd criterion) ✓
- **Classification**: RESIDENT for admissions (2 criteria met) — [1]

### Scenario 3: F-1 Student from Japan, All Schooling in Hawaii
- **High school**: Hawaii (1 criterion) ✓
- **College**: Hawaii (1 criterion) ✓
- **Classification**: RESIDENT for admissions (2 criteria met) — [1]
- **Note**: Immigration status doesn't affect admissions classification

### Scenario 4: Mainland US Applicant with No Hawaii/Pacific Ties
- **All 5 criteria**: Mainland US locations
- **Classification**: NONRESIDENT for admissions
- **Competition**: For ~10 nonresident seats — [1]

---

## Key Takeaways

1. **Ties-based system** - Not based on days of residency; 5 criteria, need 2
2. **Pacific Islands count** - 17+ Pacific Island nations/territories equal to Hawaii ties
3. **87% resident seats** - Strong preference for residents (~67 of 77 seats)
4. **No citizenship requirement** - JABSOM accepts international applicants
5. **F-1/international can be "residents"** - If they meet 2+ ties criteria
6. **Verified through applications** - AMCAS + secondary application essay
