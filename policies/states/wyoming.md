---
meta:
  state: wyoming
  abbreviation: WY
  last_verified: 2026-01-06
  complexity: medium
  has_medical_schools: false  # No independent medical school - WWAMI only
  has_public_schools: false
  # Matches index: md: 0/0, do: 0/0
  md_preference_total: 0   # WWAMI seats at UW, not a WY school
  md_preference_public: 0
  do_preference_total: 0   # No DO schools
  do_preference_public: 0

# Wyoming uses WWAMI partnership - 5-year residency requirement
admissions_residency:
  type: state_level
  physical_presence:
    required_years: 5
    consecutive: true
    school_counts: not_addressed  # Not explicitly stated in sources
  financial_independence:
    dependent_inherits_parent: true
    can_derive_from:
      - parent
      - legal_guardian

regional_program:
  name: wwami
  lead_state: washington
  member_states:
    - washington
    - wyoming
    - alaska
    - montana
    - idaho
  certification_required: true
  certification_deadline: october_15
  certification_office: wyoming_certifying_office
  contact_email: certoff@uwyo.edu
  contact_phone: "307-766-6704"

schools:
  # WWAMI partnership - seats at UW School of Medicine (not a Wyoming school)
  - name: University of Washington School of Medicine (via WWAMI)
    degree: MD
    type: public
    application_system: AMCAS
    seats_per_year: 20
    acceptance_rate: "50.0%"  # 3-year average
    interview_location: Laramie, WY
    notes:
      - "Wyoming students start at University of Wyoming in Laramie"
      - "MD degree from UW School of Medicine"
      - "Not counted as Wyoming school (prg: [wwami] in index)"

service_obligation:
  required: true
  years: 3
  location: wyoming
  alternative: repay_plus_interest
  return_rate: "62%"  # 162 of 262 graduates returned

citizenship:
  eligible:
    - us_citizen
    - permanent_resident
  ineligible:
    - f1_visa
    - j1_visa
    - canadian_citizen  # Explicitly excluded
    - other_nonimmigrant
  notes:
    - "UW School of Medicine does not accept international or Canadian students for WWAMI"

military:
  # Not clearly addressed in sources
  notes:
    - "Military service credit toward 5-year requirement not explicitly addressed"

deadlines:
  certification: october_15  # Prior year
  amcas: november  # Application deadline
  mcat_latest: september_30
---

# Wyoming Medical School Residency Research

**Last Verified**: 2026-01-06 - verified via browser

## Sources Index

| ID | Source | URL |
|----|--------|-----|
| [1] | UWyo WWAMI Admissions | https://www.uwyo.edu/wwami/applicant-information/index.html |
| [2] | UWyo WWAMI Program Overview | https://www.uwyo.edu/wwami/index.html |
| [3] | UWyo Certifying Office - WICHE/WWAMI/WYDENT | https://www.uwyo.edu/preprof/funding-your-education/wiche-wwami-wydent.html |
| [4] | UW Medicine Acceptance Statistics | https://www.uwmedicine.org/school-of-medicine/md-program/admissions/acceptance-statistics |
| [5] | UW Medicine WWAMI State Eligibility | https://www.uwmedicine.org/school-of-medicine/md-program/admissions/state-eligibility |

---

## Policy Type

**Regional Partnership (WWAMI)**: Wyoming does NOT have its own medical school. Instead, it participates in the WWAMI Regional Medical Education Program with the University of Washington School of Medicine. — [2][5]

**WWAMI States**: **W**ashington, **W**yoming, **A**laska, **M**ontana, **I**daho — [5]

---

## How WWAMI Works for Wyoming Residents — [2][5]

### Program Structure
1. **Year 1 (18 months)**: Foundations curriculum at University of Wyoming in Laramie, WY — [2]
2. **Year 2**: Complete foundations + USMLE Step 1 at UWyo, then transition to clinical clerkships
3. **Years 3-4**: Clinical rotations throughout the WWAMI region (WA, WY, AK, MT, ID) — [5]

### Degree Awarded
- **MD from University of Washington School of Medicine** — [2][5]
- Students are official UW medical students, but do early training in Wyoming

### Seats Available — [2][3]
- **20 seats per year** reserved for qualified Wyoming residents — [2]
- This is contractually guaranteed by the Wyoming-UW agreement

---

## Residency Requirements — [1][3]

### The 5-Year Rule

> "You, your parent, or your legal guardian must be a legal resident of Wyoming for **five continuous years** preceding matriculation into medical school." — [1]

### Key Points
- **5 years continuous** (not cumulative) — [1]
- Can derive residency from **parent OR legal guardian** — [1][3]
- Must be **continuous** immediately prior to matriculation
- Requires **certification** by Wyoming Certifying Office — [3]

### Certification Process — [3]

1. Apply to Wyoming WWAMI Certifying Office for residency certification
2. **Deadline**: October 15th of the year prior to anticipated enrollment — [3]
3. Applications received after deadline are **generally rejected** — [3]
4. Certification is SEPARATE from admission - can complete either first

**Contact**: Wyoming Certifying Office - certoff@uwyo.edu, 307-766-6704 — [3]

---

## Service Obligation (CONTRACT REQUIRED) — [1][3]

### The 3-Year Commitment

Wyoming WWAMI students are **required to sign a contract** stating: — [1]
- Upon completion of residency training, return to Wyoming to practice medicine for **3 years**
- OR repay the subsidized tuition cost from Wyoming state government **plus interest** — [3]

### Why This Matters
- Wyoming subsidizes WWAMI tuition significantly — [3]
- The service obligation is legally binding
- Failure to return triggers financial penalty

### Historical Data — [2]
- **162 of 262** Wyoming-WWAMI graduates have completed residency and returned to Wyoming to practice — [2]
- That's approximately **62% return rate**

---

## Citizenship/Immigration Requirements — [4]

### Eligible Applicants

| Status | Eligible? |
|--------|-----------|
| US Citizens | YES |
| US Permanent Residents | YES |

### NOT Eligible

| Status | Eligible? |
|--------|-----------|
| **F-1 Visa (Student)** | **NO** |
| **J-1 Visa (Exchange)** | **NO** |
| International Students | **NO** |
| Canadian Citizens | **NO** |

**IMPORTANT**: UW School of Medicine "does not accept international or Canadian students" for WWAMI. — [4]

---

## Acceptance Rates & Statistics — [4]

### Wyoming-Specific

| Metric | Value |
|--------|-------|
| Seats per year | 20 — [4] |
| Wyoming acceptance rate | 50.0% (3-year average) — [4] |
| Interview location | Laramie, WY |

### WWAMI Region Comparison (E-2025, 3-year average for MD only) — [4]

| Location | Acceptance Rate |
|----------|-----------------|
| Spokane (WA) | 52.2% |
| Wyoming | 50.0% |
| Alaska | 44.1% |
| Seattle (WA) | 30.4% |
| Idaho | 27.0% |
| Montana | 25.2% |
| Washington (overall) | 15.5% |
| Out-of-Region | **0.4%** |

**Key Insight**: Wyoming's 50% acceptance rate reflects the dedicated seat allocation for Wyoming residents. — [4]

---

## Application Process — [1][3]

### Timeline

| Date | Action |
|------|--------|
| October 15 (prior year) | Residency certification deadline |
| November | AMCAS application deadline |
| Throughout year | Interviews in Laramie, WY |
| Spring | Acceptance decisions |
| Fall | Matriculation at UWyo |

### Requirements — [1][3][4]

1. **AMCAS Application** to University of Washington School of Medicine — [4]
2. **Residency Certification** from Wyoming Certifying Office — [3]
3. **MCAT** taken by September 30 of year prior to matriculation — [1]
4. **Legal residence** in AMCAS must be listed as Wyoming — [1]

### Interview Format — [1]
- 30-40 minutes
- Panel of 3 interviewers
- Conducted in Laramie, WY

---

## Why WWAMI Exists — [2]

### Historical Context
- Wyoming, Alaska, Montana, and Idaho don't have population bases to support independent medical schools — [2]
- WWAMI brings medical education TO the states rather than sending all students to Seattle — [2]

### Mission
- Train physicians who will **return to practice** in underserved areas — [2]
- 162 of 262 Wyoming-WWAMI graduates have returned to practice in Wyoming (~62%) — [2]

**Note**: Additional WWAMI statistics (founding year, primary care percentages) not verified from current sources.

---

## Common Applicant Questions

### Q: I'm from Wyoming but went to college out of state. Am I eligible?
**A:** YES, if: — [1][3]
1. You have 5+ continuous years of Wyoming residency (or your parent/guardian does)
2. You are a US citizen or permanent resident
3. You get certified by October 15

### Q: My parents moved to Wyoming 3 years ago. Can I apply?
**A:** NO. The requirement is **5 continuous years**. Wait until your parent has 5 years of Wyoming residency, then you can derive eligibility from them. — [1]

### Q: I'm on an F-1 visa. Can I apply to WWAMI?
**A:** NO. WWAMI only accepts US citizens and permanent residents. F-1 visa holders are not eligible. — [4][5]

### Q: Do I have to return to Wyoming after residency training?
**A:** You are contractually obligated to either: — [1][3]
1. Return to Wyoming and practice for 3 years, OR
2. Repay the subsidized tuition cost plus interest

### Q: What if I want to do my clinical rotations in Seattle?
**A:** Clinical rotation assignments are made based on educational needs and availability. You may or may not be placed in Seattle. Many Wyoming students do rotations throughout the WWAMI region. — [2]

### Q: Is WWAMI a "separate" medical school?
**A:** NO. You are a **University of Washington School of Medicine student**. You receive a UW MD degree. WWAMI is the delivery mechanism for providing medical education across 5 states. — [2]

---

## Edge Cases to Investigate

- [ ] What happens if parents divorce and only one remains in Wyoming?
- [ ] Can military members stationed in Wyoming count toward 5-year requirement?
- [ ] What if student establishes their own 5-year residency independent of parents?
- [ ] How strictly is the service obligation enforced? What is the repayment amount?
- [ ] Can DACA recipients apply? (Not clearly addressed in sources)

---

## Key Takeaways

1. **Wyoming has no independent medical school** - WWAMI is the only path for in-state medical education
2. **5 years residency required** - Continuous residency prior to matriculation
3. **50% acceptance rate** - For Wyoming-certified applicants — [4]
4. **Service obligation is real** - 3 years practice in Wyoming or repay
5. **US citizens/permanent residents ONLY** - No international or Canadian students — [4]
6. **Certification is separate from admission** - Apply to certifying office by October 15
7. **Early training in Wyoming** - First 18 months at UWyo, not Seattle
