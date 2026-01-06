---
meta:
  state: texas
  abbreviation: TX
  last_verified: 2026-01-06
  complexity: medium
  has_medical_schools: true
  has_public_schools: true
  # Matches index: md: 13/11, do: 2/2
  md_preference_total: 13  # 12 TMDSAS + TCU (AMCAS); 90% rule for TMDSAS
  md_preference_public: 11 # All public (Baylor and TCU are private)
  do_preference_total: 2   # UNT TCOM, Sam Houston (TMDSAS)
  do_preference_public: 2  # Both public; UIW uses AACOMAS so excluded

# Texas uses TMDSAS for centralized ADMISSIONS residency determination
# Tuition residency is determined separately at matriculation
admissions_residency:
  type: domicile_based
  determination_by: TMDSAS  # Centralized for all participating schools
  centralized_system: TMDSAS
  pathways:
    - type: high_school_graduation
      requirements:
        texas_hs_graduation_or_ged: true
        months_in_texas_before_graduation: 36
        months_in_texas_by_deadline: 12
    - type: domicile_establishment
      requirements:
        months_in_texas_by_deadline: 12
        domicile_methods:
          - gainful_employment
          - property_ownership
          - business_ownership
          - marriage_to_resident
  physical_presence:
    required_months: 12
    deadline: october_1
  financial_independence:
    dependent_inherits_parent: true
    can_establish_own_while_dependent: false

marriage_transfer:
  enabled: true
  spouse_domicile_required_months: 12
  marriage_duration_required_months: 12

schools:
  # MD Schools (TMDSAS unless noted)
  - name: Baylor College of Medicine
    degree: MD
    type: private
    application_system: TMDSAS
    daca_accepted: false
    regional_preference: none
    notes: "Private school - same evaluation criteria for in-state and out-of-state, but in-state acceptance rate (~4.9%) is higher than out-of-state (~1.8%)"

  - name: McGovern Medical School at UTHealth Houston
    degree: MD
    type: public
    application_system: TMDSAS
    daca_accepted: false
    regional_preference: none
    secondary_required: true
    casper_required: true

  - name: Texas A&M School of Medicine
    degree: MD
    type: public
    application_system: TMDSAS
    daca_accepted: true
    regional_preference: rural_underserved
    special_programs:
      - name: RUP2M (Rural and Underserved Populations to Medicine)
        eligibility: "Must reside in rural, medically underserved, primary care, or health professional shortage area (HRSA designated)"
        target: "TAMU system sophomores considering medicine from underserved areas"
        benefit: "Conditional admission to medical school"
    mission_focus: "Rural populations, underserved communities, primary care"

  - name: Texas Tech University Health Sciences Center (Lubbock)
    degree: MD
    type: public
    application_system: TMDSAS
    daca_accepted: false
    regional_preference: west_texas
    secondary_question: "Do you consider yourself from West Texas or as having West Texas ties? If yes, what town or county did you reside in, or what other factors would you cite?"
    mission_focus: "West Texas, rural health care, 108 counties of West Texas"
    notes: "20% of practicing physicians in West Texas are TTUHSC alumni"

  - name: Texas Tech Paul L. Foster School of Medicine (El Paso)
    degree: MD
    type: public
    application_system: TMDSAS
    daca_accepted: false
    regional_preference: us_mexico_border
    secondary_question: "Recognizing the components of this mission and that PLFSOM is located on the US/Mexico border, please describe why you are interested in applying to our school."
    mission_focus: "Border health, Hispanic health, underserved border communities"
    notes: "First four-year medical school on US/Mexico border; experience with Hispanic populations is valuable"

  - name: Tilman J. Fertitta Family College of Medicine (UH)
    degree: MD
    type: public
    application_system: TMDSAS
    daca_accepted: false
    regional_preference: se_texas_houston
    mission_fit_screening: true
    secondary_questions:
      - "Prior experience in primary care settings (general internal medicine, pediatrics, or family medicine)"
      - "Experience in medical practice or social service for underserved areas"
      - "Experience in community or public health"
      - "Why are you interested in the primary care field(s) and care of the community as a whole?"
    mission_focus: "Primary care physician shortage, SE Texas, W Louisiana, urban and rural underserved areas"
    notes: "Screens for mission fit before sending secondary; class size only 60; Early Decision available for applicants committed to primary care in Houston area"

  - name: UT Southwestern Medical Center
    degree: MD
    type: public
    application_system: TMDSAS
    daca_accepted: false
    regional_preference: none
    secondary_required: true
    casper_required: true
    notes: "No explicit Dallas regional preference found; serves high-need populations across Dallas and North Texas"

  - name: UT Medical Branch (UTMB)
    degree: MD
    type: public
    application_system: TMDSAS
    daca_accepted: false
    regional_preference: galveston_gulf_coast
    secondary_questions:
      - "Are there particular characteristics of our school and/or the Galveston area in terms of location, history, or other attributes that make you especially interested in matriculating here?"
    casper_required: true
    duet_required: true  # Pilot program
    mission_focus: "Galveston County, Gulf Coast Region"

  - name: UT Rio Grande Valley School of Medicine
    degree: MD
    type: public
    application_system: TMDSAS
    daca_accepted: false
    regional_preference: rio_grande_valley
    video_requirement:
      duration: "2 minutes"
      prompt: "Select 2 of 5 values (patient advocacy, community focus, cultural awareness, collaborative leadership, lifelong problem solving) and discuss what you have done that resonates with them"
    class_composition: "96% Texas residents"
    mission_focus: "Transform healthcare in Rio Grande Valley, diverse communities of South Texas, social justice, community engagement"

  - name: UT San Antonio Long School of Medicine
    degree: MD
    type: public
    application_system: TMDSAS
    daca_accepted: true
    regional_preference: south_texas
    mission_statement: "Particular sensitivity to and focus on the South Texas region"
    notes: "Foremost medical educator in South Texas; no secondary application; CASPer and one-way video interview required"
    casper_required: true

  - name: UT Austin Dell Medical School
    degree: MD
    type: public
    application_system: TMDSAS
    daca_accepted: false
    regional_preference: central_texas_mission
    secondary_type: video_response  # Not written, video-based
    mission_focus: "Central Texas community, person-centered integrated care"
    notes: "No written secondary; video-response secondary sent to screened applicants"

  - name: UT Tyler School of Medicine
    degree: MD
    type: public
    application_system: TMDSAS
    daca_accepted: false
    regional_preference: east_texas
    regional_preference_tiers:
      - tier: 1
        description: "Direct ties to East Texas (born, graduated high school, community college, undergraduate, etc.)"
      - tier: 2
        description: "Indirect ties to East Texas (family members, in-laws, visited frequently, attended summer camp, etc.)"
      - tier: 3
        description: "Ties to a rural region with similar characteristics to East Texas"
      - tier: 4
        description: "No ties but interested in practicing in East Texas after graduation"
      - tier: 5
        description: "No ties but still interested in attending"
    secondary_question: "Please indicate your connection to East Texas as outlined in our county map and explain"
    mission_focus: "East Texas rural and underserved communities, primary care, preventive health"
    class_size: 40
    notes: "First medical school in East Texas; very small class makes admission highly competitive"

  - name: TCU Burnett School of Medicine
    degree: MD
    type: private
    application_system: AMCAS
    regional_preference: none
    minimum_hours_required:
      service: 150
      leadership: 150
      physician_patient_interaction: 150
      personal_excellence: 150
    casper_required: true
    duet_required: true
    notes: "Uses AMCAS, not TMDSAS; no written secondary (audio-recorded answers); Fort Worth community mission but no explicit regional preference"

  # DO Schools
  - name: UNT Texas College of Osteopathic Medicine
    degree: DO
    type: public
    application_system: TMDSAS
    daca_accepted: false
    regional_preference: none
    secondary_required: true
    secondary_fee: 50
    notes: "90% Texas residents required by law; no explicit regional preference within Texas"

  - name: Sam Houston State College of Osteopathic Medicine
    degree: DO
    type: public
    application_system: TMDSAS
    daca_accepted: true
    regional_preference: eastern_texas
    mission_focus: "Increase physician workforce in eastern region of Texas, primary care, rural practice"
    secondary_questions:
      - "What do you like or dislike most about the area you are from (your hometown or where you graduated high school)?"
      - "What do you consider the role of physicians in medically underserved Texas communities?"
    selection_criteria:
      - "Availability of physicians in applicant's region of residence (underserved or shortage area)"
      - "Alignment to SHSU and COM mission statement"
    notes: "Recruits from areas where applicants would likely return to practice"

  - name: University of the Incarnate Word School of Osteopathic Medicine
    degree: DO
    type: private
    application_system: AACOMAS
    regional_preference: inland_empire_south_texas
    mission_focus: "South Texas, underserved communities, health equity"
    notes: "Uses AACOMAS - excluded from TMDSAS 90% rule; first faith-based osteopathic school in Texas; bilingual applicants should self-identify"

citizenship:
  eligible:
    - us_citizen
    - permanent_resident
    - conditional_permanent_resident
    - pending_i485
    - refugee
    - asylee
    - parolee
    - temporary_protected_status
    - daca
    - h1b_visa
    - h4_visa
    - e_visa
    - l_visa
    - o1_visa
    - o3_visa
  ineligible:
    - f1_visa
    - f2_visa
    - j1_visa
    - j2_visa
    - tn_visa
    - td_visa

military:
  home_of_record_texas: automatic_resident
  claimed_texas_12_months: resident_with_les_proof
  spouse_included: true
  dependents_included: true
  temporary_absence_protected: true

nonresident_cap:
  percentage: 10
  enforced_by: law  # Texas law limits non-residents to 10% of entering class
  note: "90% of seats reserved for Texas residents"

deadlines:
  application: october_1
  residency_period_start: october_1_prior_year
---

# Texas Medical School Residency Research

**Last Verified**: 2026-01-06 - all key claims confirmed from TMDSAS official sources

## Sources Index

| ID | Source | URL |
|----|--------|-----|
| [1] | TMDSAS Residency Application Guide | https://www.tmdsas.com/application-guide/residency.html |
| [2] | TMDSAS Residency Determination | https://www.tmdsas.com/explore/residency.html |
| [3] | Texas Higher Education Coordinating Board | https://www.highered.texas.gov/texas-residency/ |
| [4] | Baylor College of Medicine Tuition Status | https://www.bcm.edu/education/registrar/tuition-status-texas-residency |
| [5] | THECB Visa Eligibility (PDF) | https://apps.highered.texas.gov/DocID/PDF/0440.PDF |
| [6] | University of Houston Visa FAQ | https://gethelp.uh.edu/kb/478 |
| [7] | Texas A&M Immigration Status | https://aggie.tamu.edu/billing-and-payments/residency-for-in-state-tuition/immigration-status |

---

## Policy Type

**Centralized State Policy**: All Texas medical schools use TMDSAS for residency determination. TMDSAS determines residency for ADMISSION purposes based on Texas Higher Education Coordinating Board rules. Tuition residency is determined separately at matriculation. — [1][2]

---

## Admissions Preference

> "Texas law limits non-residents to maximum 10% of entering class" in dental, medical, podiatric, and veterinary programs. — [2]

This means **90% of seats are reserved for Texas residents** - a massive in-state advantage.

---

## Two Pathways to Establish Residency

### Option 1: Texas High School Graduation Route — [1][2]

**Eligible for:** US citizens, permanent residents, and international students with qualifying visa types

**Requirements (ALL must be met):**
1. Graduate from a Texas high school OR obtain GED in Texas
2. Live in Texas for 36 consecutive months immediately before high school graduation
3. Maintain 12 consecutive months of Texas residence by application deadline (October 1)

### Option 2: Domicile Establishment Route — [1][2][3]

**Eligible for:** US citizens, permanent residents, those with pending permanent residency applications, and international students with approved visa types

**Requirements:**
1. Live in Texas for 12 consecutive months by application deadline (October 1), AND
2. Establish AND maintain domicile for 12 consecutive months through ONE of these methods:
   - **Gainful employment** in Texas
   - **Sole or joint marital ownership** of residential real property in Texas
   - **Own and operate a business** in Texas
   - **Marriage for one year** to a person who has established domicile in Texas

---

## Marriage Rule (Detailed)

**Texas allows residency transfer through marriage.** — [1][2]

To establish residency through marriage:
- Your spouse must have established AND maintained domicile in Texas for 12 months prior to the application deadline
- You must have been married for at least one year
- Documentation required: Texas Marriage Certificate or Declaration of Registration of Informal Marriage

**Example scenario:**
- Spouse has lived and worked in Texas since January 2023
- You married spouse in January 2024
- By October 2024 application deadline: Spouse has 21 months of domicile, you have 9 months of marriage
- Result: NOT YET ELIGIBLE (need 12 months married)
- By October 2025: NOW ELIGIBLE (12+ months married to domiciled spouse)

---

## Dependent vs Independent Students

### Dependent Students — [1]
- A dependent student's residency is based on their parent's or legal guardian's residency
> "If the parent or court-appointed legal guardian of a dependent student meets the criteria of having established residency for tuition purposes, the dependent student is eligible to pay resident tuition" — [1]
- **CRITICAL**: "If your parents claim you and they live in another state, you are not eligible to establish residency while being claimed as a dependent" — [1]

### Independent Students — [1][3]
- Can establish residency independently through Option 2 (domicile)
- Must NOT be claimed as a dependent on parent's federal income taxes

### How to Become Independent
To be classified as independent, you generally need to:
- Be 18+ years old
- NOT be claimed as a dependent on anyone's federal taxes
- Support yourself financially

---

## Military Exemptions — [1][3]

### Home of Record = Texas
- Military member is **presumed to be a Texas resident**
- Spouse and dependent children also qualify
- No additional requirements

### Home of Record ≠ Texas BUT Claimed Texas Residence
- Must provide Leave and Earnings Statements (LES) showing Texas claimed as place of residence for 12 consecutive months prior to enrollment
- If requirements met: presumed Texas resident (self, spouse, dependents)
- If not: classified as Non-Texan for admission purposes

### Temporary Absence for Military Service
- Temporary absence from Texas for military service does NOT affect domicile status
- Must provide documentation of reason for absence
- Applies to: US Armed Forces, Public Health Service, Department of Defense, US Department of State

---

## DACA and Undocumented Students

### DACA Application Process — [1]
1. Select "None" for visa type/residency status
2. In Optional Question section, indicate DACA status
3. Complete the Residency Affidavit
4. Documentation required: valid Texas driver's license, EAD, or other DHS documentation

### Schools That DO NOT Accept DACA Applicants — [1] (verified 2026-01-06)

The following schools **only consider US citizens or permanent residents** (12 schools):
- Baylor College of Medicine
- John Sealy School of Medicine at UTMB
- McGovern Medical School at UTHealth Houston
- Texas Tech University Health Sciences Center (Lubbock)
- Texas Tech Paul L. Foster School of Medicine (El Paso)
- Tilman J. Fertitta Family College of Medicine (University of Houston)
- UNT Texas College of Osteopathic Medicine
- UT Austin Dell Medical School
- UT Rio Grande Valley School of Medicine
- UT Southwestern Medical Center
- UT Tyler School of Medicine
- UT RGV School of Podiatric Medicine

### Schools That DO Accept DACA Applicants — [1]

The following schools accept DACA applicants (verify directly - policies can change):
- **Texas A&M School of Medicine**
- **UT San Antonio Long School of Medicine**
- **Sam Houston State College of Osteopathic Medicine**

---

## International Students

### Eligible Immigration Statuses — [5]

**Permanent/Immigrant Statuses:**
- US Citizen
- Permanent Resident (Green Card holder)
- Conditional Permanent Resident
- Pending I-485 (adjustment of status application filed)
- Refugee
- Asylee
- Parolee
- Temporary Resident
- Temporary Protected Status (TPS) - must be granted, not just applied
- VAWA petitions (approved for spouse/children)
- Approved USCIS I-360
- DACA (Deferred Action)

**Eligible Nonimmigrant Visa Types:** — [5]
- **A** - Diplomats and foreign government officials
- **E** - Treaty traders/investors (E-1, E-2)
- **G** - International organization representatives
- **H-1B** - Specialty occupation workers
- **H-4** - Dependents of H-1B holders
- **I** - Foreign media representatives
- **K** - Fiancé(e) of US citizen
- **L** - Intracompany transferees (L-1A, L-1B)
- **N** - NATO officials
- **NATO** - NATO personnel
- **O-1** - Extraordinary ability individuals
- **O-3** - Dependents of O-1 holders
- **R** - Religious workers
- **T** - Trafficking victims
- **U** - Crime victims
- **V** - Spouse/child of permanent resident

### Ineligible Visa Types — [5][6]
- **F-1** - Student visa
- **F-2** - Dependent of F-1
- **J-1** - Exchange visitor
- **J-2** - Dependent of J-1
- **TN** - NAFTA professional (Canadian/Mexican)
- **TD** - Dependent of TN

### Documentation Requirements for Eligible Visa Holders — [5][6][7]
Example for H-4 dependent:
- Valid H-4 visa
- Valid H-1B visa for the spouse/parent
- Letter of employment showing full-time employment for at least 12 consecutive months

---

## Timeline Requirements — [1][2]

| Deadline | Requirement |
|----------|-------------|
| October 1 (prior year) | Start of 12-month residency period |
| October 1 (application year) | Must have 12 consecutive months of Texas residence |
| October 1 (application year) | Must have 12 consecutive months of domicile (Option 2) |
| October 1 (application year) | TMDSAS application deadline |

**For Option 1 (HS graduation):**
- Need 36 months Texas residence before HS graduation (historical)
- Plus 12 months continuous residence by October 1 deadline

---

## Documentation Requirements — [1]

For domicile establishment (Option 2), may need to provide:
- Texas driver's license (showing 12 months at Texas address)
- Texas voter registration
- Texas vehicle registration
- Proof of gainful employment (pay stubs, employment letter)
- Property deed or mortgage documents
- Business registration documents
- Marriage certificate (if claiming through spouse)
- Leave and Earnings Statements (military)
- EAD card (DACA)

---

## Common Applicant Questions

### Q: I went to undergrad in Texas for 4 years. Am I a Texas resident?
**A:** Not automatically. It depends on:
- Were you claimed as a dependent by parents in another state? → Likely NOT a Texas resident
- Did you establish domicile (gainful employment, property, etc.)? → Possibly a Texas resident
- Did you graduate from a Texas high school with 36 months prior residence? → Possibly via Option 1

### Q: My parents moved to Texas while I was in college out of state. Am I a resident?
**A:** If you're still claimed as a dependent: YES, you may derive residency from your parents if they've established Texas domicile for 12 months by the deadline.

### Q: I'm getting married to a Texan. When can I claim residency?
**A:** You need:
1. Your spouse to have 12 months of established domicile in Texas
2. To be married for at least 12 months
Both must be true by the October 1 application deadline.

### Q: I have a Texas driver's license. Am I a resident?
**A:** A Texas driver's license alone does not establish residency. It's one piece of documentation, but you must also meet the physical presence and domicile requirements.

### Q: I'm on an F-1 visa and have lived in Texas for 4 years. Am I a resident?
**A:** Generally NO. F-1 visa holders cannot establish permanent domicile in the US, which is required for residency classification.

### Q: My DACA status was just approved. Can I apply to all Texas medical schools?
**A:** NO. Most Texas medical schools (12 of 15) only accept US citizens or permanent residents. Only Texas A&M, UT San Antonio Long, and Sam Houston State accept DACA applicants. — [1]

---

---

## School-Specific Regional Preferences

**IMPORTANT**: Beyond Texas residency, many schools have their own regional preferences within Texas. These are evaluated through secondary applications and mission fit.

### Regional Preference Map

| School | Region | Preference Strength |
|--------|--------|---------------------|
| **UT Tyler** | East Texas | Strong (tiered system in secondary) |
| **Texas Tech Lubbock** | West Texas | Strong (explicit secondary question) |
| **Texas Tech El Paso** | US-Mexico Border | Strong (explicit secondary question) |
| **UTRGV** | Rio Grande Valley | Strong (96% TX, video on RGV values) |
| **UT San Antonio Long** | South Texas | Moderate (mission statement) |
| **UH Fertitta** | SE Texas/Houston | Strong (screens for mission fit) |
| **UTMB** | Galveston/Gulf Coast | Moderate (secondary question) |
| **Dell** | Central Texas | Moderate (mission focus) |
| **Texas A&M** | Rural/Underserved | Moderate (RUP2M program) |
| **SHSU-COM** | Eastern Texas | Strong (mission: eastern region workforce) |

### UT Tyler - East Texas Regional Preference

The secondary application asks applicants to classify their East Texas connection in tiers:

1. **Tier 1 (Strongest)**: Direct ties - born there, graduated high school, attended community college or undergrad
2. **Tier 2**: Indirect ties - family members, in-laws, visited frequently, attended summer camp
3. **Tier 3**: Similar rural region ties - from an area with similar characteristics
4. **Tier 4**: No ties but want to practice there after graduation
5. **Tier 5**: No ties, still interested in attending

**Tip**: If you have ANY East Texas connection, document it thoroughly.

### Texas Tech Schools - West Texas & Border

**Lubbock (TTUHSC)** asks directly: "Do you consider yourself from West Texas or as having West Texas ties?"
- If yes: Describe the town/county and other factors
- 20% of practicing West Texas physicians are TTUHSC alumni

**El Paso (Foster)** asks about border interest: "PLFSOM is located on the US/Mexico border, please describe why you are interested..."
- Experience with Hispanic populations is particularly valuable
- Focus on border health disparities

### UH Fertitta - Primary Care Mission Screening

UH Fertitta **screens applications before sending secondaries** for mission fit:
- Primary care commitment (family medicine, internal medicine, pediatrics)
- SE Texas / W Louisiana service interest
- Underserved population experience

**Early Decision** available for applicants certain about primary care in Houston area.

### UTRGV - Rio Grande Valley

Requires a 2-minute video selecting 2 of 5 values:
- Patient advocacy
- Community focus
- Cultural awareness
- Collaborative leadership
- Lifelong problem solving

96% of class are Texas residents. Strong preference for RGV community connection.

### SHSU-COM (DO) - Eastern Texas

Mission explicitly states: "increase the physician workforce in the eastern region of Texas"

Secondary asks:
- What do you like/dislike about your hometown area?
- Role of physicians in medically underserved Texas communities?

Selection considers: availability of physicians in your region of residence.

---

## Edge Cases to Investigate

- [ ] What qualifies as "gainful employment"? Part-time? How many hours?
- [ ] Can online business ownership count for domicile?
- [ ] What if parents are divorced and one lives in Texas, one out of state?
- [ ] Graduate students - are they presumed independent like in California?
- [ ] What happens if marriage ends during medical school?

---

## Key Takeaways

1. **90% reserved for residents** - Texas law caps non-residents at 10%
2. **Marriage can transfer residency** - Spouse must have 12mo domicile, you must be married 12mo
3. **Two pathways** - HS graduation route OR domicile establishment
4. **Dependents inherit parent's state** - Cannot independently establish while claimed as dependent
5. **DACA varies by school** - Only 3 of 15 schools accept DACA (Texas A&M, UTSA Long, Sam Houston)
6. **F-1/J-1 cannot establish residency** - Not eligible for Texas residency classification
7. **October 1 deadline** - All residency requirements must be met by this date
8. **TMDSAS centralizes** - One system determines residency for all TMDSAS schools
9. **Regional preferences exist** - Many schools prefer applicants from specific Texas regions (East, West, South, Border, Gulf Coast)
10. **Mission fit matters** - UH Fertitta screens for primary care commitment before sending secondaries
11. **Secondary questions reveal preferences** - UT Tyler, Texas Tech schools, UTMB explicitly ask about regional ties
