---
meta:
  state: washington
  abbreviation: WA
  last_verified: 2026-01-06
  complexity: high
  has_medical_schools: true
  has_public_schools: true
  # Matches index: md: 2/2, do: 1/0
  md_preference_total: 2   # UW, WSU Elson Floyd (both public)
  md_preference_public: 2
  do_preference_total: 1   # PNWU-COM (private, regional preference)
  do_preference_public: 0  # PNWU is private

# Washington has TWO schools with different rules: UW (WWAMI lead) and WSU (WA-only)
admissions_residency:
  type: school_specific  # UW and WSU have different rules
  physical_presence:
    required_months: 12
    school_counts: false
    credit_limit_while_establishing: 6  # Per term limit
  financial_independence:
    dependent_inherits_parent: true

regional_program:
  name: wwami
  role: lead_state
  member_states:
    - washington
    - wyoming
    - alaska
    - montana
    - idaho

schools:
  # MD Schools
  - name: University of Washington School of Medicine
    degree: MD
    type: public
    application_system: AMCAS
    program_type: wwami_lead
    class_size: 280
    seats_by_location:
      seattle: 100
      spokane: 60
      wyoming: 20
      alaska: 30
      montana: 30
      idaho: 40
    acceptance_rates:
      washington_overall: "15.5%"
      seattle: "30.4%"
      spokane: "52.2%"
      wyoming: "50.0%"
      alaska: "44.1%"
      montana: "25.2%"
      idaho: "27.0%"
      out_of_region: "0.4%"
    citizenship:
      eligible:
        - us_citizen
        - permanent_resident
        - daca  # If verified by state
      ineligible:
        - f1_visa
        - j1_visa
        - canadian_citizen  # Without green card
        - other_nonimmigrant
    out_of_region:
      eligible_with_ties: true
      requires_disadvantaged_or_service: true
      ties_criteria:
        - tribal_affiliation_wwami
        - born_in_wwami
        - hs_graduation_wwami
        - family_in_wwami
        - lived_1_year_wwami
        - military_stationed_wwami
        - pre_med_programs
    notes:
      - "MSTP (MD/PhD) is NOT restricted to WWAMI residents"
      - "DACA recipients must be verified by state residency office"

  - name: WSU Elson S. Floyd College of Medicine
    degree: MD
    type: public
    application_system: AMCAS
    program_type: state_only
    class_size: 80
    washington_only: true
    regional_preference: rural_underserved
    rural_background_percentage: 15.3
    eligibility_pathways:
      ties_to_washington:
        criteria_needed: 3
        criteria:
          - born_in_washington
          - childhood_address_washington
          - hs_graduation_washington
          - parent_lives_washington
      legal_residency:
        required_months: 12
        deadline: january_1
    secondary_question: "What experiences have you had with rural and/or underserved communities? What have you learned? (300 words)"
    mission_focus: "Rural, underserved, historically marginalized, and vulnerable populations in Washington"
    campus_locations: ["Everett", "Spokane", "Tri-Cities", "Vancouver"]
    citizenship:
      eligible:
        - us_citizen
        - permanent_resident
      ineligible:
        - f1_visa
        - j1_visa
        - daca  # Not mentioned as eligible
        - other_nonimmigrant
    notes:
      - "100% of class from Washington or with significant ties"
      - "DACA NOT explicitly included as eligible"
      - "15.3% of students have childhood rural county backgrounds"
      - "Community-based medical education model - students train in existing community clinics/hospitals"

  # DO Schools
  - name: Pacific Northwest University of Health Sciences (PNWU-COM)
    degree: DO
    type: private
    application_system: AACOMAS
    regional_preference:
      states: [alaska, idaho, montana, oregon, washington]
    notes:
      - "Private school with regional preference for AK/ID/MT/OR/WA"
      - "Counted in do: 1/0 (total/public) - has preference but is private"

citizenship:
  notes:
    - "UW accepts DACA if verified by state"
    - "WSU does NOT mention DACA as eligible"
    - "Neither school accepts international or Canadian students"

military:
  active_duty_exempt: true
  wa_national_guard_exempt: true
  notes:
    - "Active military stationed in WA qualifies for residency"
    - "WA National Guard members qualify"

deadlines:
  uw_residency_establish_by: june_22  # For following year entry
---

# Washington Medical School Residency Research

**Last Verified**: 2026-01-06 - verified via browser

## Sources Index

| ID | Source | URL |
|----|--------|-----|
| [1] | UW Medicine WWAMI State Eligibility | https://www.uwmedicine.org/school-of-medicine/md-program/admissions/state-eligibility |
| [2] | UW Registrar - Medical Students Residency | https://registrar.washington.edu/residency-groups/med-students/ |
| [3] | WSU Elson S. Floyd College of Medicine Admissions | https://medicine.wsu.edu/md/apply/requirements/ |
| [4] | WSU ESFCOM FAQs | https://medicine.wsu.edu/md/apply/faqs/ |
| [5] | UW Medicine MD Admissions | https://www.uwmedicine.org/school-of-medicine/md-program/admissions |
| [6] | UW Medicine Acceptance Statistics | https://www.uwmedicine.org/school-of-medicine/md-program/admissions/acceptance-statistics |

---

## Policy Type

**TWO DISTINCT MEDICAL SCHOOLS** with different eligibility rules:
1. **University of Washington School of Medicine** - WWAMI regional program (5-state)
2. **WSU Elson S. Floyd College of Medicine** - Washington-only program

---

# SCHOOL 1: University of Washington School of Medicine (WWAMI)

## Overview

- **Program Type**: Regional medical education partnership (WWAMI) — [1]
- **States Served**: Washington, Wyoming, Alaska, Montana, Idaho — [1]
- **Class Size**: 280 total (E-2025), ~95% from WWAMI region — [6]
- **Terminology**: Uses "out-of-region" not "out-of-state" — [1]

## Residency Requirements for Washington Residents — [2]

### The 12-Month Rule

> "You must have maintained a primary residence in Washington for at least **12 consecutive months** immediately prior to your first admitted quarter." — [2]

### Key Requirements — [2]

- Residence must be for purposes **other than postsecondary education** — [2]
- For 2026 applicants: Must establish residence by **June 22, 2025** — [2]
- If taking courses at WA college during prior 12 months: Cannot exceed 6 credits/term — [2]
- If exceed 6 credits: Must prove residence for reasons other than education — [2]

### Verification Process — [2]

1. Must affirm US citizen or permanent resident status — [2]
2. Submit affidavit if meeting standard requirements — [2]
3. Submit Residence Questionnaire if not meeting standard requirements — [2]
4. Financially dependent students can claim residency through parent/guardian — [2]

## WWAMI State Eligibility — [1]

### How It Works
- Legal state of residence in AMCAS determines WWAMI eligibility — [1]
- WWAMI states (WY, AK, MT, ID) require **separate state certification** — [1]
- Each WWAMI state has its own residency requirements (see individual state files)

### WWAMI State Seat Allocation — [6]

| State | Seats/Year | Foundation Site |
|-------|------------|-----------------|
| Seattle (WA) | 100 | Seattle |
| Spokane (WA) | 60 | Spokane |
| Wyoming | 20 | University of Wyoming, Laramie |
| Alaska | 30 | University of Alaska, Anchorage |
| Montana | 30 | Montana State University, Bozeman |
| Idaho | 40 | University of Idaho, Moscow |

**Note**: Approximately 10 of Seattle's seats per year are for MSTP (MD/PhD). — [6]

### MSTP (MD/PhD) Exception — [5]

**IMPORTANT**: The Medical Scientist Training Program (MSTP) is NOT restricted to WWAMI residents:
> "Selection for this program is national in scope and is not restricted to residents of Washington, Wyoming, Alaska, Montana or Idaho." — [5]

- MSTP applicants must be U.S. citizens or permanent residents — [5]
- DACA recipients are only eligible for "MD only program" (not MSTP) — [5]

## Out-of-Region Eligibility — [1][5]

### Requirements (BOTH must be met)

Out-of-region applicants are considered if they meet **BOTH** of the following: — [5]

1. **Ties to WWAMI** (at least one): — [1]
   - Member of federally recognized tribe whose traditional boundaries include WWAMI states
   - Born in a WWAMI state
   - Graduated from high school in a WWAMI state
   - Have family members who currently live in a WWAMI state
   - Currently live and/or have lived in a WWAMI state for at least one year
   - Active military stationed in WWAMI region
   - Participated in pre-med programs (SHPEP, SMDEP) or sponsored by WWAMI partner institutions
   - Other ties (option available in application) — [1]

2. **AND at least one of**: — [5]
   - Service record with underserved communities
   - From an economically or educationally disadvantaged background

### Out-of-Region Acceptance Rate — [6]
- **0.4%** (extremely competitive) — [6]
- Based on 3-year average for MD program only

### Acceptance Rates by State (E-2025, 3-year average) — [6]

| State/Region | Acceptance Rate |
|--------------|-----------------|
| Washington | 15.5% |
| — Seattle | 30.4% |
| — Spokane | 52.2% |
| Wyoming | 50.0% |
| Alaska | 44.1% |
| Idaho | 27.0% |
| Montana | 25.2% |
| Out-of-Region | 0.4% |

## Citizenship/Immigration Requirements — [5][6]

### Eligible

| Status | Eligible? |
|--------|-----------|
| US Citizens | YES — [5] |
| US Permanent Residents | YES — [5] |
| DACA Recipients | YES, if reside in WWAMI state AND legally authorized by state's residency office — [5][6] |

### NOT Eligible

| Status | Eligible? |
|--------|-----------|
| **International Students** | **NO** — [6] |
| **Canadian Citizens/PRs (without US green card)** | **NO** — [6] |
| **F-1 Visa** | **NO** (implied by above) |
| **J-1 Visa** | **NO** (implied by above) |

**Direct quotes from sources:**
- "Applicants must have United States citizenship or permanent residency (green card)." — [5]
- "International and Canadian applicants without a green card will not be considered." — [5]
- "We do not accept international or Canadian students." — [6]
- "Applicants with Deferred Action for Childhood Arrivals (DACA) who reside in a WWAMI state and who are legally authorized and recognized by their state's residency office as a resident for WWAMI educational purposes will be considered for admission to the MD only program." — [5]

---

# SCHOOL 2: WSU Elson S. Floyd College of Medicine

## Overview — [3]

- **Program Type**: Washington state-only (no regional partnership) — [3]
- **Class Size**: 80 students from Washington — [3]
- **Tuition**: Same for all admitted students — [3]
- **100% of class** from Washington or with significant ties — [3]

## Two Pathways to Eligibility — [3]

### Pathway 1: "Ties to Washington" (3 of 4 Criteria)

Must meet **at least 3 of these 4 criteria**: — [3]

| # | Criterion |
|---|-----------|
| 1 | **Born** in Washington |
| 2 | **Childhood address** in Washington |
| 3 | **Graduated from high school** in Washington |
| 4 | **Parent/guardian currently lives** in Washington |

**Note**: This pathway works regardless of AMCAS legal residence state. — [3]

> "Regardless of the identified state of residency on AMCAS, if you demonstrate that you are 'from Washington' by meeting at least 3 of these 4 ties to Washington, you meet this requirement." — [3]

### Pathway 2: Legal Washington Residency — [3]

- Must meet WA "resident student" definition per RCW 28B.15.012(2) — [3]
- Must be resident for **12-month period** leading to **January 1** of enrollment year — [3]
- Requires documentation verification — [3]

Options for resident student definition: — [3]
- Financially independent with bona fide domicile for 1 year by January 1
- Financially dependent with parent/guardian with domicile for 1 year by January 1
- Active military stationed in WA or WA National Guard member
- Member of federally recognized tribe with traditional boundaries in WA (with domicile in ID, MT, OR, or WA)

### What Happens If You Don't Qualify — [3][4]

> "Applicants who do not meet the definition of a Washington resident student or do not have 3 or more ties to Washington are **not eligible** for admission and will not receive a secondary application." — [3]

> "If you do not meet any of these requirements, you will not be considered and will not receive a secondary application." — [4]

## Citizenship Requirements — [3][4]

### Eligible

| Status | Eligible? |
|--------|-----------|
| US Citizens | YES — [3] |
| US Permanent Residents | YES — [3] |

### NOT Eligible

| Status | Eligible? |
|--------|-----------|
| F-1 Visa | **NO** — [4] |
| J-1 Visa | **NO** — [4] |
| International Students | **NO** — [4] |
| DACA | **NOT ELIGIBLE** (not mentioned as exception) — [3][4] |

**Direct quotes:**
- "U.S. Citizen or U.S. Permanent Resident" required — [3]
- "We only accept applications from U.S. citizens and those with valid U.S. permanent resident cards (green cards)." — [4]

**Note**: Unlike UW Medicine, WSU ESFCOM does NOT mention DACA as an eligible category. Their citizenship requirement explicitly states "U.S. citizen or permanent resident" without DACA exception. — [3][4]

---

## Key Differences Between Schools

| Factor | UW Medicine | WSU ESFCOM |
|--------|-------------|------------|
| Regional vs State | WWAMI (5 states) — [1] | Washington only — [3] |
| Out-of-state possible? | Yes (WWAMI + limited out-of-region) — [1] | NO — [3][4] |
| "Ties" pathway | Yes (out-of-region, requires disadvantaged/service) — [1][5] | Yes (3 of 4 criteria, standalone) — [3] |
| Class size | 280 — [6] | 80 — [3] |
| Tuition differential | Yes (resident vs non) | No (all pay in-state) — [3] |
| DACA eligible | YES (with state verification) — [5] | NO (not mentioned) — [3][4] |

---

## Common Applicant Questions

### Q: I'm a Washington resident. Which school should I apply to?
**A:** You can apply to BOTH:
- UW Medicine (WWAMI) - larger program, regional scope — [1][6]
- WSU ESFCOM - smaller, Washington-focused, rural/underserved emphasis — [3]

### Q: I was born in Washington but moved away as a child. Can I apply to WSU?
**A:** Possibly. Count your criteria per [3]:
- Born in WA: 1 point
- Childhood address in WA: 1 point (if applicable)
- HS graduation in WA: 0 points if graduated elsewhere
- Parent in WA: 1 point if applicable
If you meet 3 of 4, you're eligible. — [3]

### Q: I'm from Idaho. Can I apply to WSU ESFCOM?
**A:** NO. WSU ESFCOM is Washington-only. — [3][4] Idaho residents should apply to UW Medicine through the WWAMI program. — [1]

### Q: I'm on an F-1 visa living in Washington. Can I apply?
**A:** NO to either school. — [4][5][6]
- UW Medicine: "Applicants must have United States citizenship or permanent residency" — [5]
- WSU ESFCOM: "We only accept applications from U.S. citizens and those with valid U.S. permanent resident cards" — [4]

### Q: I have DACA status and live in Washington. Can I apply?
**A:**
- **UW Medicine**: YES, if verified as resident by Washington state — [5]
- **WSU ESFCOM**: NO - they specify "US citizen or permanent resident" without mentioning DACA — [3][4]

### Q: I'm from California but my parents now live in Washington. Can I apply anywhere?
**A:**
- **UW Medicine**: Possibly as out-of-region with ties (family in WWAMI state), BUT you also need disadvantaged background OR underserved service record. Very competitive (0.4% acceptance). — [1][5][6]
- **WSU ESFCOM**: Count your criteria per [3]. If parent lives in WA = 1 point. Need 2 more (born in WA? childhood in WA? HS in WA?). If only 1-2 criteria, NOT eligible. — [3]

---

## Edge Cases to Investigate

- [ ] What exactly counts as "childhood address" for WSU ties pathway?
- [ ] How does WSU verify the 4 ties criteria?
- [ ] Can military stationed in WA use ties pathway or only legal residency pathway?
- [ ] What documentation does UW require for DACA verification?

---

## Key Takeaways

### For Washington Residents:
1. **Apply to both schools** - They have different missions and may evaluate you differently
2. **UW Medicine** is larger with regional scope — [1][6]
3. **WSU ESFCOM** is smaller, focused on rural/underserved Washington — [3]

### For WWAMI State Residents (WY, AK, MT, ID):
1. **Apply to UW Medicine** through WWAMI — [1]
2. **Get state certification** by your state's deadline — [1]
3. **WSU ESFCOM is NOT an option** - Washington-only — [3]

### For Out-of-Region Applicants:
1. **UW Medicine requires BOTH** ties to WWAMI AND (disadvantaged background OR underserved service) — [1][5]
2. Extremely competitive: 0.4% acceptance rate — [6]
3. **WSU ESFCOM NOT possible** unless you have 3+ ties to Washington specifically — [3]

### For International Students:
1. **Neither school accepts international students** — [5][6][4]
2. Must have US citizenship or permanent residency (green card) to apply — [5][4]
3. Canadian citizens/PRs without green card are NOT eligible — [5][6]

### For DACA Recipients:
1. **UW Medicine**: Eligible if in WWAMI state and verified by state residency office — [5]
2. **WSU ESFCOM**: NOT eligible - not mentioned as exception to citizenship requirement — [3][4]
