---
meta:
  state: california
  abbreviation: CA
  last_verified: 2026-01-06
  complexity: very_high
  has_medical_schools: true
  has_public_schools: true
  # Matches index: md: 6/5, do: 0/0
  md_preference_total: 6   # 5 UC + CUSM (Inland Empire regional preference)
  md_preference_public: 5  # UC schools
  do_preference_total: 0   # CA DO schools are private with no state preference
  do_preference_public: 0

# California uses 366-day domicile rule for classification
admissions_residency:
  type: domicile_based
  determination_by: school  # Each UC school handles residency
  required_days: 366
  school_counts: false  # Educational presence doesn't count
  continuous: true

financial_independence:
  grad_students_presumed_independent: true
  dependent_inherits_parent: false

intent:
  timing: "more_than_one_year_before"
  required_docs:
    - drivers_license
    - voter_registration
    - vehicle_registration
  supporting_docs:
    - state_tax_returns
    - bank_accounts
    - lease_or_property
  relinquish_other_state_license: true

schools:
  # MD schools with preference (5 UC public + 1 CUSM private)
  - name: UCSF School of Medicine
    degree: MD
    type: public
    application_system: AMCAS
    class_size: 161
    resident_percentage: 77  # Updated: 71-77% range
    regional_preference: california_statewide
    acceptance_rates:
      in_state: "3.1-3.2%"
      out_of_state: "0.8-1.0%"
    mission_focus: "Health equity, underserved populations, PRIME-US track"
    citizenship:
      eligible:
        - us_citizen
        - permanent_resident
        - daca
      ineligible:
        - f1_visa
        - j1_visa
        - international
    notes: "Strong CA preference (77% of class); in-state applicants 4x more likely to be admitted"

  - name: UCLA David Geffen School of Medicine
    degree: MD
    type: public
    application_system: AMCAS
    regional_preference: none_stated
    eligibility_requirement: "Must be US citizen, permanent resident, DACA recipient, OR California resident"
    acceptance_rates:
      in_state: "2.17%"
      out_of_state: "1.03%"
      international: "1.86%"
    citizenship:
      eligible:
        - us_citizen
        - permanent_resident
        - daca
        - california_resident  # Alternative eligibility if not citizen/PR/DACA
    notes: "Claims no state preference in evaluation, but CA residency is an alternative eligibility criterion; 42% of applicants are in-state"

  - name: UC Davis School of Medicine
    degree: MD
    type: public
    application_system: AMCAS
    regional_preference: northern_central_california
    resident_percentage: 96
    secondary_focus: "Northern/Central California connection"
    special_programs:
      - name: Rural-PRIME
        focus: "Rural California communities"
        target_specialties: ["Primary Care", "Family Medicine", "Pediatrics", "OB/GYN", "General Surgery", "Emergency Medicine"]
    advantage_factors:
      - "Northern/Central California ties"
      - "Rural or medically underserved area origin"
    citizenship:
      notes: "Welcomes undocumented and DACA students"
    notes: "96% CA residents; out-of-state may not receive secondary; 80%+ of graduates remain in CA"

  - name: UC Irvine School of Medicine
    degree: MD
    type: public
    application_system: AMCAS
    regional_preference: none_explicit
    resident_percentage: 83.3
    mission_focus: "Orange County's multicultural communities"
    notes: "Officially claims no state preference, but 83% of class are CA residents; serves Orange County (one of most medically underserved yet demographically rich regions)"

  - name: UC Riverside School of Medicine
    degree: MD
    type: public
    application_system: AMCAS
    regional_preference: inland_southern_california
    resident_percentage: 90
    acceptance_rate: "1.35%"
    special_programs:
      - name: Thomas Haider Program
        eligibility: "Deep local ties to Inland Empire"
        benefit: "Scholarship with 5-year Inland Empire practice commitment"
    mission_focus: "Inland Southern California, medically underserved communities"
    citizenship:
      notes: "Explicitly welcomes undocumented and DACA students"
    notes: "90% have ties to Inland SoCal; only considers out-of-state with significant CA relationship; community-based education from Year 1"

  - name: California University of Science and Medicine (CUSM)
    degree: MD
    type: private
    application_system: AMCAS
    regional_preference: inland_empire
    resident_percentage: 98
    inland_empire_percentage: 31
    acceptance_rate: "2.05%"
    mission_focus: "Inland Empire physician shortage, underserved areas"
    notes: "Private school with strong Inland Empire preference; 98% CA residents, 31% from Inland Empire; Spanish for Healthcare Professionals offered; founded to address <35 PCPs per 100k in Inland Empire"

citizenship:
  eligible:
    - us_citizen
    - permanent_resident
    - refugee
    - asylee
    - daca_ab540
  ineligible:
    - f1_visa
    - f2_visa
    - j1_visa
    - j2_visa
    - b1_visa
    - b2_visa
    - h2_visa
    - h3_visa
    - m_visa
    - tn_visa
    - td_visa
  notes:
    - "F-1/J-1 cannot establish domicile"
    - "AB540 provides exemption for qualifying undocumented students"

military:
  active_duty_resident: true
  spouse_included: true
  dependents_included: true
  veteran_va_benefits: true
---

# California Medical School Admissions Residency

**Last Verified**: 2026-01-06

## Sources Index

| ID | Source | URL |
|----|--------|-----|
| [1] | UCSF Registrar - California Residency | https://registrar.ucsf.edu/registration/residency |
| [2] | UC Residency Requirements (UCOP) | https://www.ucop.edu/residency/residency-requirements.html |
| [3] | UC Riverside Medical School - Undocumented Students | https://somsa.ucr.edu/admissionsundocumented |
| [4] | UC Davis Medical School - Undocumented Applicants | https://health.ucdavis.edu/mdprogram/admissions/undocumented-applicants.html |
| [5] | UCSF Admissions Data | https://meded.ucsf.edu/about-us/program-statistics/admissions-data |

---

## Admissions Classification System

California uses a **366-day domicile rule** to classify applicants as California residents or non-residents. This classification is used by UC medical schools and affects your applicant pool positioning.

### Core Requirements — [1][2]

1. **Physical Presence**: 366+ days continuous in California
2. **Intent**: Documented intent to make California permanent home
3. **Not for School**: Presence for educational purposes does NOT count
4. **Timing**: Intent actions must be completed more than 1 year before enrollment

---

## Class Composition — [5]

**UCSF (Fall 2025):**

| Statistic | Value |
|-----------|-------|
| California Residents | **71%** |
| Total Applications | 10,300 |
| Total Matriculated | 161 |
| Overall Acceptance Rate | 1.6% |

**Note**: Individual school policies vary:
- **UCSF**: Strong CA resident preference (71% of class)
- **UCLA**: Claims to review "without consideration of state of residence" but CA resident eligibility is a criterion
- **UCI**: Uses same evaluation criteria for in-state and out-of-state

---

## School Attendance Does NOT Count — [1][2]

**CRITICAL WARNING**:

Presence in California **solely for educational purposes** does NOT establish residency, regardless of duration.

**Example**: 4 years of undergrad at a California school does NOT make you a California resident.

To become a resident, you need 366 days of NON-educational presence (working, living, etc.).

---

## Graduate Students Are Independent — [2]

UC treats graduate/professional students differently from undergrads:

- **Presumed financially independent**: Evaluated on YOUR residency, not your parents'
- **No inheritance from parents**: Unlike undergrads, you don't automatically inherit parent's state
- **Your actions matter**: Your path to CA residency is based on YOUR physical presence and intent

---

## Citizenship Requirements

### Can Apply to UC Medical Schools

| Status | Eligible? |
|--------|-----------|
| US Citizens | YES |
| US Permanent Residents | YES |
| DACA Recipients | YES |
| Refugees | YES |
| Asylees | YES |
| AB540 (Undocumented) | YES |

### Cannot Establish Residency — [1]

| Status | Can Establish Residency? |
|--------|--------------------------|
| F-1 Visa (Student) | NO |
| J-1 Visa (Exchange) | NO |
| B-1/B-2 (Tourist) | NO |
| TN/TD (NAFTA) | NO |
| Other Nonimmigrant | NO |

**Note**: F-1/J-1 holders CAN apply to UC medical schools but cannot establish California residency.

---

## DACA and Undocumented Students — [3][4]

**UC medical schools explicitly welcome DACA and undocumented students:**

> "UC Davis School of Medicine will continue to welcome and support pre-medical and medical students without regard to immigration status." — [4]

> "UCR School of Medicine explicitly welcomes undocumented and DACA students. Applications considered under same standards as other applicants." — [3]

**AB540 Requirements:**
- Attended California high school for 3+ years
- Graduated from California high school or obtained GED in California
- Filed affidavit stating intent to legalize status when eligible

---

## Military Classification — [2]

| Category | Resident Classification? |
|----------|--------------------------|
| Active duty stationed in CA | YES |
| Spouse of active duty in CA | YES |
| Dependents of active duty in CA | YES |
| Veterans using VA benefits | YES |

---

## Common Scenarios

### Scenario 1: Undergrad in California
- **Situation**: Attended UCLA for 4 years, now applying to UC medical schools
- **Classification**: NON-RESIDENT (educational presence doesn't count)
- **To become resident**: Need 366 days of working/living in CA NOT for school

### Scenario 2: Parents in California
- **Situation**: Parents live in CA, you went to college out of state
- **Classification**: Evaluated on YOUR residency (grad students are independent)
- **Note**: Parent's CA residence doesn't automatically transfer to you

### Scenario 3: Gap Year in California
- **Situation**: Took gap year working in CA before medical school
- **Classification**: Potentially RESIDENT if 366+ days with proper intent documentation
- **Key**: Must not be "primarily for educational purposes"

### Scenario 4: F-1 Student
- **Situation**: International student on F-1 visa
- **Classification**: Can APPLY but CANNOT establish CA residency
- **Result**: Will be classified as non-resident regardless of time in California

---

---

## School-Specific Regional Preferences

Beyond California residency, several UC schools have regional preferences within California:

### Regional Preference Summary

| School | Regional Focus | Preference Strength | Key Evidence |
|--------|----------------|---------------------|--------------|
| **UC Davis** | Northern/Central CA | Strong | Secondary asks about N/Central CA connection |
| **UC Riverside** | Inland Southern CA | Strong | 90% have Inland SoCal ties |
| **CUSM** | Inland Empire | Strong | 98% CA, 31% Inland Empire specifically |
| **UCSF** | Statewide CA | Moderate | 77% CA, PRIME-US for underserved |
| **UCLA** | None stated | Weak | Claims no preference, but CA eligibility criterion |
| **UCI** | None explicit | Weak | 83% CA but claims no preference |

### UC Davis - Northern/Central California

**Secondary Question**: "Do you have a connection to Northern or Central California? If 'yes', please explain (500 characters)"

UC Davis highly values applicants with connections to Northern California, particularly the Sacramento area. The admissions committee explicitly looks for:
- Northern/Central California ties
- Geographic origin from rural or medically underserved areas
- Interest in serving communities they describe as their focus region

**Rural-PRIME Program**: For students interested in becoming physician leaders in rural California communities:
- Weekly seminars and leadership training
- Rural physician mentorship
- Clinical rotations in rural communities
- Target specialties: Primary Care, Family Medicine, Pediatrics, OB/GYN, General Surgery, Emergency Medicine

**Important**: Out-of-state applicants may not receive a secondary application. 96% of matriculants are California residents.

### UC Riverside - Inland Southern California

UC Riverside has an explicit mission to serve Inland Southern California:
- 90% of students have ties to Inland Southern California
- Only considers out-of-state applicants who can demonstrate significant California relationship
- Community-based education model embeds students in San Bernardino and Riverside from Year 1

**Thomas Haider Program**: For students with deep local ties to Inland Empire
- Scholarship recipients commit to practicing in Inland Empire for 5 years after residency

### CUSM - Inland Empire (Private)

California University of Science and Medicine was founded specifically to address the Inland Empire's physician shortage (<35 PCPs per 100,000 residents):
- 98% of students are California residents
- 31% are specifically from the Inland Empire
- Spanish for Healthcare Professionals offered to serve local community
- 66% of graduates perform residency in Southern California
- 28% remain in the Inland Empire

---

## Key Takeaways

1. **366 days required** - Must be continuous, immediately prior to enrollment
2. **School attendance does NOT count** - Biggest trap for applicants
3. **Grad students are independent** - Evaluated on your own residency, not parents'
4. **F-1 can apply but can't be resident** - Will always be classified as non-resident
5. **DACA/undocumented welcome** - UC schools explicitly accept these applicants
6. **77% in-state at UCSF** - Strong practical advantage for CA residents
7. **Intent must be 1+ year before** - Documentation required early
8. **Regional preferences matter** - UC Davis (Northern CA), UC Riverside (Inland SoCal), CUSM (Inland Empire) have explicit regional focuses
9. **Secondary questions reveal preferences** - UC Davis asks specifically about N/Central CA connection
