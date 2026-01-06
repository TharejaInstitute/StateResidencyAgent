---
meta:
  state: west_virginia
  abbreviation: WV
  last_verified: 2026-01-06
  complexity: medium
  has_medical_schools: true
  has_public_schools: true
  # Matches index: md: 2/1, do: 1/1
  md_preference_total: 2   # WVU (public), Marshall (state-assisted)
  md_preference_public: 1  # WVU only; Marshall is state-assisted
  do_preference_total: 1   # WVSOM (public)
  do_preference_public: 1

# West Virginia has school-specific rules: Marshall (bordering states) vs WVU (ties-based)
admissions_residency:
  type: school_specific  # Marshall and WVU have different preferences
  physical_presence:
    required_months: 12
    school_counts: false
    continuous: true
  financial_independence:
    dependent_inherits_parent: true

schools:
  # MD Schools
  - name: Marshall University Joan C. Edwards School of Medicine
    degree: MD
    type: state_assisted
    application_system: AMCAS
    instate_percentage: 57.3
    outstate_percentage: 42.7
    mcat_average: 506
    gpa_average: 3.81
    application_fees:
      instate: 75
      outstate: 100
    citizenship:
      eligible:
        - us_citizen
        - permanent_resident
      ineligible:
        - f1_visa
        - j1_visa
        - daca  # Not explicitly included
        - other_nonimmigrant
    preferences:
      - tier: 1
        criteria: West Virginia residents
        secondary_auto_sent: true
      - tier: 2
        criteria: Bordering states
        states:
          - kentucky
          - maryland
          - ohio
          - pennsylvania
          - virginia
        secondary_auto_sent: true
        notes: "Strongly considered"
      - tier: 3
        criteria: Non-bordering with competitive application
        secondary_auto_sent: conditional

  - name: WVU School of Medicine
    degree: MD
    type: public
    application_system: AMCAS
    outstate_percentage: 50  # Approximate
    citizenship:
      eligible:
        - us_citizen
        - permanent_resident
        - daca
        - international  # With restrictions
      ineligible:
        - international_coursework  # No international coursework accepted
    preferences:
      - tier: 1
        criteria: West Virginia residents
      - tier: 2
        criteria: Pathway programs
      - tier: 3
        criteria: Strong ties or mission fit
        ties_examples:
          - previous_wv_residency
          - family_in_wv

  # DO Schools
  - name: West Virginia School of Osteopathic Medicine (WVSOM)
    degree: DO
    type: public
    application_system: AACOMAS
    regional_preference: rural_primary_care
    mission_focus: "West Virginia and rural areas, primary care"
    secondary_questions:
      - "Why do you want to be an osteopathic physician? (500 char)"
      - "What advantage do you see in attending WVSOM over other medical schools? (500 char)"
      - "What experiences (living, working or visiting) have you had in rural areas? (500 char)"
      - "Describe an ethically challenging situation you have been in, and how you responded (500 char)"
    screening_criteria:
      minimum_science_gpa: 3.0
      minimum_mcat: 490
      competitive_science_gpa: 3.2
      competitive_mcat: 495
    secondary_fee: 0
    interview_fee:
      in_state: 0
      out_of_state: 80
    citizenship:
      eligible:
        - us_citizen
        - permanent_resident
      notes:
        - "DACA/international policy requires verification from WVSOM directly"
    preferences:
      - tier: 1
        criteria: West Virginia residents
      - tier: 2
        criteria: Rural background or experience
    selection_criteria:
      - "Motivation for osteopathic medicine"
      - "Motivation to serve in rural communities in primary care fields"
      - "Health-related experiences"
      - "Scholastic achievement"
    notes:
      - "Participates in Choose WV Practice Program"
      - "Public osteopathic medical school in Lewisburg, WV"
      - "Very mission-oriented - wants students from rural communities or with rural service experience"
      - "WV ties can be beneficial in admissions"

citizenship:
  notes:
    - "Marshall (MD): US citizens or permanent residents only"
    - "WVU (MD): Explicitly accepts DACA and international students"
    - "WVU (MD): Does not accept international coursework"
    - "WVSOM (DO): Verify citizenship policy directly with school"

military:
  veterans_gi_bill_exempt: true
  notes:
    - "Veterans using Chapter 30 or Chapter 33 VA benefits qualify for in-state status"

special_programs:
  - name: Choose West Virginia Practice Program
    applies_to:
      - marshall
      - wvsom
      - wvu
    eligibility: out_of_state_only
    when_to_apply: during_medical_school
    preference: first_year_students
    deadline: november_15
    benefit: "~30000_per_year"
    total_potential: "~120000_over_4_years"
    obligation:
      years_of_service: matches_years_of_funding
      max_years: 4
      timing: within_6_months_of_training_completion
      locations: rural_or_shortage_specialty
    penalty: repay_plus_5_percent_interest
---

# West Virginia Medical School Residency Research

**Last Verified**: 2026-01-06 - verified via official Marshall Policy PDF and federal IPEDS data

## Sources Index

| ID | Source | URL |
|----|--------|-----|
| [1] | Marshall Admissions Criteria | https://jcesom.marshall.edu/admissions/admissions-criteria/ |
| [2] | Marshall MD Admission Policy (Official PDF) | https://jcesom.marshall.edu/media/63690/2025_policydocument.pdf |
| [3] | WVU Ask the Admissions Team | https://medicine.wvu.edu/md-admissions/ask-the-admissions-team/ |
| [4] | WVU Tuition and Aid | https://medicine.wvu.edu/md-admissions/tuition-and-aid/ |
| [5] | Choose WV Practice Program | https://health.wvu.edu/rural-health/financial-incentives/choose-west-virginia-practice-program/ |
| [6] | Marshall Class Profiles | https://jcesom.marshall.edu/admissions/profile-of-entering-students/ |
| [7] | WVU BOG Residency Rule 2.4 | https://policies.wvu.edu/finalized-bog-rules/bog-academics-rule-2-4-residency-status-for-admission-tuition-and-fee-purposes |
| [8] | College Tuition Compare (Federal IPEDS Data) | https://www.collegetuitioncompare.com/medical-schools/joan-c-edwards-school-of-medicine-at-marshall-university/ |

---

## Medical Schools in West Virginia

| School | Degree | Type | Focus |
|--------|--------|------|-------|
| **WVU School of Medicine** | MD | Public | Large state school, broad mission |
| **Marshall University Joan C. Edwards School of Medicine** | MD | State-assisted | Rural health, Central Appalachia focus |
| **West Virginia School of Osteopathic Medicine (WVSOM)** | DO | Public | Osteopathic medicine, primary care |

---

# SCHOOL 1: Marshall University Joan C. Edwards School of Medicine

## Mission

> "A community-based, Veterans Affairs affiliated medical school dedicated to providing high quality medical education and postgraduate training programs to foster a skilled physician workforce to meet the unique healthcare needs of West Virginia and Central Appalachia."
> — Source: [1]

## Citizenship Requirements

**Eligible:** US citizens or permanent residents only
> "All applicants must be U.S. citizens or have permanent resident visas."
> — Source: [1]

**NOT Eligible:**
- F-1 visa holders
- J-1 visa holders
- Other nonimmigrant visas
- DACA status (not explicitly included in eligible categories)

## Admissions Preference — [2]

> "As a state assisted medical school, MUJCESOM gives admissions preference to West Virginia residents. **Bordering state residents (Kentucky, Maryland, Ohio, Pennsylvania, and Virginia) will be strongly considered.** Applicants are considered only if they are U.S. citizens or have permanent resident visas."
> — Source: [2] (Official Policy PDF)

### Secondary Application Process — [2]

> "Supplemental application will be automatically forwarded to applicants with a verified AMCAS application who are residents of West Virginia and applicants who are residents of bordering states (Kentucky, Ohio, Virginia, Pennsylvania and Maryland). Nonresident applicants from non-bordering states who have competitive applications will be forwarded a supplemental application."
> — Source: [2]

**Key Points:**
- WV residents and bordering state residents **automatically** receive secondary applications
- Non-bordering state applicants with competitive applications may also receive secondaries
- MD/PhD applicants receive secondary regardless of residency if program requirements met

### Application Fees
- West Virginia residents: $75 (non-refundable)
- Non-residents: $100 (non-refundable)
- AMCAS fee waiver recipients: Fee waived
> — Source: [2]

### Class Composition (Federal IPEDS Data) — [8]
- **57.3%** West Virginia residents
- **42.7%** Out-of-state residents

### Entering Class Statistics (Class of 2025) — [6]
- Average MCAT: 506
- Average GPA: 3.81

**Note**: Marshall does not publicly publish MCAT minimums or acceptance rates by residency status on their website. The Policy PDF directs applicants to "see website for MCAT score cut-offs" but this information is not publicly posted.

## Deadlines and Requirements — [1]

**MCAT Timing:**
> "The MCAT must be taken within three calendar years prior to matriculation."
> — Source: [1]

**Letters of Recommendation Deadline:**
> "All letters must be submitted through AMCAS by December 15 of the year prior to matriculation."
> — Source: [1]

## Exceptions to MCAT Requirement — [1]

> "The only exceptions are applicants from Marshall University's Early Assurance Program and BS/MD Program who meet specific program criteria, who are exempt from the MCAT requirement."
> — Source: [1]

---

# SCHOOL 2: WVU School of Medicine

## Admissions Philosophy — [3]

**50% Out-of-State:**
> "For the past several years, approximately half of each medical student class has been composed of students who are residents of states other than West Virginia."
> — Source: [3]

## Priority System — [3]

### Priority 1: West Virginia Residents
> "West Virginia residents have the highest priority"
> — Source: [3]

### Priority 2: Pathway Programs
> "Residents of other states in one of their established pathway programs are also given high priority"
> — Source: [3]

### Priority 3: Strong Ties / Mission Fit
> "Residents of other states with strong ties (including but not limited to personally residing in West Virginia or having family members living in West Virginia) or who meet their mission are encouraged to apply."
> — Source: [3]

## Citizenship Requirements — [3]

**DACA and International Students:**
> "International and DACA students may apply...International and DACA students who meet their requirements are eligible to apply and are considered out-of-state applicants."
> — Source: [3]

**Key Difference from Marshall:** WVU explicitly accepts DACA and international students; Marshall does not.

**Important Restriction:**
> "WVU School of Medicine does not accept international coursework."
> — Source: [3]

## Definition of "Strong Ties" — [3]

> "Strong ties (including but not limited to personally residing in West Virginia or having family members living in West Virginia)"
> — Source: [3]

**Note:** "Having ties does not guarantee an interview."
> — Source: [3]

## State Residency Rules — [7]

**12-Month Rule:**
> "Domicile within West Virginia is established when a student, the student's spouse, or (for dependent students) their parent(s) or legal guardian have maintained a continuous presence of at least 12 months within the state prior to the start of classes, provided that such presence must be for some primary purpose that does not include enrollment at the University."
> — Source: [7]

**Dependent Students:**
> "A dependent student maintains the same domicile as that of their parent(s) or legal guardian."
> — Source: [7]

**Veterans:**
> "Veterans using Chapter 30 or Chapter 33 VA benefits qualify for in-state status."
> — Source: [7]

---

# SPECIAL PROGRAM: Choose West Virginia Practice Program

## What It Is — [5]

A tuition waiver program for OUT-OF-STATE medical students who commit to practicing in West Virginia after graduation.

> "Tuition waivers to encourage nonresident medical students to stay and practice in the state after graduation."
> — Source: [5]

## Financial Benefit — [5]

> "Awards cover approximately $30,000 annually—the difference between in-state and out-of-state tuition."
> — Source: [5]

**Total Potential Benefit:** ~$120,000 over 4 years

## Eligibility Requirements — [5]

**Who Can Apply:**
> "Students accepted or enrolled at Marshall University, West Virginia School of Osteopathic Medicine, or West Virginia University in a program leading to a Doctor of Medicine or Doctor of Osteopathy degree who meet institutional requirements for being classified as an out-of-state student"
> — Source: [5]

**Key Points:**
1. Must be classified as OUT-OF-STATE (not for in-state students)
2. Must not be in default on previous student loans
3. First-year medical students receive preference
4. Students from any year may apply

## Application Process — [5]

**When to Apply:** During medical school (not before admission)
> "First-year medical students receive preference, though students from any class year may apply."
> — Source: [5]

**Deadline:**
> "Application Deadline: November 15, 2024" [for 2024-25 cycle]
> — Source: [5]

**This is NOT part of the standard admissions application.** It is a separate program you apply to after being admitted and classified as out-of-state.

## Service Obligation — [5]

> "Recipients must practice at an eligible West Virginia site for one year of service...for each year of funding received (maximum four years)."
> — Source: [5]

**Timeline:**
> "The obligation begins within six months after completing residency or fellowship training."
> — Source: [5]

**Eligible Practice Sites:**
> "Designated rural areas or any West Virginia site offering shortage specialties like family practice, emergency medicine, psychiatry, and pediatrics."
> — Source: [5]

## Consequences of Non-Compliance — [5]

> "If obligations aren't met, participants must repay received funds plus five percent interest accruing from the date training is completed or terminated."
> — Source: [5]

---

## Applicant Decision Tree

### For Out-of-State Applicants Considering WV Schools

#### Step 1: Determine Citizenship Eligibility

| Your Status | Marshall | WVU |
|-------------|----------|-----|
| US Citizen | Eligible | Eligible |
| Permanent Resident | Eligible | Eligible |
| DACA | NOT eligible | Eligible (out-of-state) |
| International (F-1/J-1) | NOT eligible | Eligible (out-of-state) |

#### Step 2: Consider Choose WV Program

**If you're out-of-state and get accepted:**
- Apply to Choose West Virginia Practice Program in Year 1
- Could save ~$120,000 in exchange for 4-year service commitment
- Must be willing to practice in WV rural/shortage areas

---

## Common Applicant Questions

### Q: What counts as "strong ties" to West Virginia?
**A:** Per WVU [3]:
- Personally residing in West Virginia
- Having family members living in West Virginia
- Note: "Having ties does not guarantee an interview"

### Q: I'm a DACA recipient. Can I apply to WV medical schools?
**A:** Per [1][3]:
- **Marshall:** NOT explicitly listed as eligible (requires "US citizens or permanent residents")
- **WVU:** YES, explicitly states "International and DACA students may apply"

### Q: I'm an international student (F-1). Can I apply?
**A:** Per [1][3]:
- **Marshall:** NO ("US citizens or permanent residents" only)
- **WVU:** YES, but no international coursework accepted, and you're out-of-state for tuition

### Q: What is the Choose WV Practice Program and when do I apply?
**A:** Per [5]:
- It's a tuition waiver program for OUT-OF-STATE students only
- You apply AFTER being admitted (not during initial application)
- First-years get preference; deadline is typically mid-November
- Gives ~$30K/year toward closing in-state/OOS tuition gap
- Requires 1 year of WV practice per year of funding (max 4 years)
- Practice must be in rural areas or shortage specialties

---

## Comparison Table

| Factor | Marshall (MD) | WVU (MD) | WVSOM (DO) |
|--------|---------------|----------|------------|
| Type | State-assisted | Public | Public |
| Application System | AMCAS | AMCAS | AACOMAS |
| WV resident preference | Yes — [2] | Yes — [3] | Yes |
| Bordering state preference | Yes (KY, MD, OH, PA, VA) — [2] | Not explicitly tiered | Not documented |
| DACA accepted | No — [2] | Yes — [3] | Verify with school |
| International accepted | No — [2] | Yes — [3] | Verify with school |
| MCAT average | 506 — [6] | Not specified | Not specified |
| OOS % of class | 42.7% — [8] | ~50% — [3] | Not specified |
| Choose WV eligible | Yes — [5] | Yes — [5] | Yes — [5] |

---

## Edge Cases to Investigate

- [ ] How strictly does Marshall enforce "US citizens or permanent residents"? Any exceptions?
- [ ] What exactly counts as "strong ties" beyond family?
- [ ] How competitive is the Choose WV program? How many awards per year?
- [ ] Can you lose Choose WV funding if you change specialties?
- [ ] WVSOM: What is their DACA/international student policy?
- [ ] WVSOM: Do they have bordering state preferences like Marshall?
- [ ] WVSOM: What is their class composition (in-state vs OOS)?

---

## Key Takeaways

1. **Three schools: 2 MD + 1 DO** - WVU and Marshall (MD via AMCAS), WVSOM (DO via AACOMAS)
2. **Different citizenship rules** - WVU accepts DACA/international; Marshall does not; WVSOM TBD
3. **Marshall: Bordering states advantage** - KY, MD, OH, PA, VA automatically get secondaries
4. **WVU: 50% out-of-state** - More open to non-WV residents than many state schools
5. **Choose WV program** - Up to $120K savings for OOS students (all 3 schools eligible)
6. **Service commitment is real** - 1 year practice per year of Choose WV funding
7. **12 months for residency** - Standard requirement, school attendance doesn't count
8. **No international coursework at WVU** - Despite accepting international students
