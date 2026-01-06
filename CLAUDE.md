# State Residency Agent - Project Instructions

## File References

When referencing files in responses:
- Always use clickable markdown links: [filename](path/to/file)
- For specific lines: [filename:42](path/to/file#L42)
- For line ranges: [filename:10-25](path/to/file#L10-L25)
- Use relative paths from the project root

---

## Project Goal

AI agent helping medical school applicants understand state residency status and which schools give them an advantage.

---

## The Confabulation Problem

**FUNDAMENTAL ERROR**: Claude can generate content that LOOKS like verified research (source tables, inline citations, direct quotes) but is actually confabulated from training data.

The format of well-cited research is easy to generate. But generating the FORMAT ≠ doing the WORK.

**When you write "[1]", that's not a record of verification - it's just text you generated.**

### The Core Rule

**You cannot produce research OUTPUT without doing research INPUT.**

A citation must be a RECORD of verification, not a FORMATTING ELEMENT.

### Required Process

For EVERY claim with a citation:

```
1. READ the source (Read/WebFetch/browser) in THIS conversation
2. DOCUMENT what you actually see: "This page shows: [actual content]"
3. WRITE the claim based ONLY on what you documented
4. CITE the source you just read
```

**NEVER**:
```
1. Write claim with citation based on training knowledge
2. Maybe verify later
```

### Signs You're Confabulating

- Writing Sources Index before visiting URLs
- Statistics (percentages, rates, counts) without seeing them on a page
- Direct quotes ("...") for text you didn't copy from visible content
- Multiple [#] citations without multiple preceding read actions
- Filling in "what seems right" based on general knowledge
- Writing research-formatted output as your FIRST action

### Correct Workflow

**WRONG**: "Let me write up the research..." → generates full document

**RIGHT**: "Let me visit the source first..." → reads page → "I see on this page: [content]" → writes claim with citation → repeats for each source

---

## Research Standards

### Completeness

For every rule/program, answer:
- WHO qualifies?
- HOW to apply? (when in process?)
- WHEN deadline?
- WHAT benefits/obligations?

### Specificity

BAD: "eligible visas include..." / "special provisions may apply"
GOOD: Complete lists, exact criteria, quoted definitions

### Distinguish

- ADMISSION eligibility vs TUITION eligibility (often different)
- State-level vs school-specific policies
- Dependent vs independent student rules

---

## Source Requirements

1. **Medical school specific**: Never use undergrad/general sources for med school policy
2. **Verifiable**: Every claim needs source URL
3. **Authoritative**: Prefer official sources (school admissions, state boards, legislature)
4. **Current**: Note date of policy documents

### Source Hierarchy

Prefer sources in this order:
1. Medical school's own admissions pages
2. State registrar/residency office pages
3. State legislature (RCW, statutes)
4. University system-wide policies

### Invalid Sources

- **Undergraduate campus registrars** - policies may differ from medical schools
- **General university admissions pages** - unless specifically for medical school
- **State financial aid commission pages** - these are for undergrad aid, not medical school

**Rule**: Every source cited must be from a medical school's own website OR a state/system policy document that explicitly applies to medical schools.

---

## Citation & Verification Process

### Citation Format

```markdown
## Sources Index
| ID | Source | URL |
|----|--------|-----|
| [1] | Descriptive Name | https://exact-url.edu/path |
| [2] | Another Source | https://another-url.edu/path |
```

### Inline Citation Format

```markdown
- Factual claim here — [1]
- "Direct quote from source" — [2]
- Claim supported by multiple sources — [1][3]
```

### Verification Rules

1. **Before adding ANY citation**:
   - Actually visit the source URL
   - Verify the specific claim exists on that page
   - If WebFetch returns 403/blocked, use Playwright browser instead

2. **Citation requirements**:
   - Every factual claim must have an inline citation — [#]
   - Direct quotes must include exact text from source
   - Citations must point to the SPECIFIC page where info appears

3. **Multi-page sources**:
   - Create separate source entries for each distinct URL
   - Don't assume information on one page exists on another

### Common Mistakes to Avoid

1. **Don't assume source content** - A URL labeled "Eligibility" may not contain class sizes or tuition
2. **Don't conflate similar pages** - "Admissions" and "Statistics" pages are different sources
3. **Don't add citations while editing** - Read/verify FIRST, then update
4. **Verify before correcting** - Re-verify when updating existing citations

---

## Verification Checklist

Before marking a research file as verified:
- [ ] All URLs in Sources Index are valid (actually visit each one)
- [ ] Each citation points to content actually on that page
- [ ] Acceptance rates/class sizes from statistics page, not general admissions
- [ ] Citizenship requirements verified from admissions eligibility page
- [ ] Tuition figures verified from official tuition page
- [ ] Direct quotes match source text exactly
- [ ] DACA/international policies verified school-by-school
- [ ] File status updated with verification date

### Verification Date Protocol

When updating research files:
1. Update status: `**Status**: Draft - verified via browser YYYY-MM-DD`
2. Note any data that couldn't be verified
3. If claim cannot be verified, remove it or add uncertainty marker

---

## Critical Rules

### MSAR Is NOT a Valid Source

**MSAR (Medical School Admission Requirements) is NOT publicly available data.** Claude never had access to MSAR during training.

Any claims that appear to be from MSAR were confabulated. Common confabulated MSAR data includes:
- MCAT minimums/preferred scores by residency status
- Acceptance rates broken down by in-state vs out-of-state
- Specific county/regional preferences
- Detailed class composition percentages

**Rule**: If data cannot be found on a medical school's public website, official policy PDFs, or federal data sources (IPEDS, AAMC public data), mark it as "not publicly available."

### Search for Official Policy Documents

Medical schools often have **official policy PDFs** with more detail than public web pages.

**Before marking claims unverifiable:**
1. Search for official policy PDFs (e.g., "MD Admission Policy")
2. Check the school's media/documents folders
3. Look for LCME accreditation documents
4. Search for the specific claim with quotes + school name

**Workflow**:
1. Check website pages first
2. Search for official policy PDFs
3. If still not found, search web for school + specific claim
4. Only mark as "not publicly available" after exhaustive search

### Verify EVERY Claim

**THIS IS A REPEATED MISTAKE. DO NOT SKIP THIS.**

When verifying research files:
- **DO NOT** verify only "key structural claims" or "main points"
- **DO** verify EVERY SINGLE claim that has a citation
- **DO** verify EVERY statistic, percentage, rate, figure
- **DO** verify EVERY visa type listed (F-1, J-1, H-1B, etc.)
- **DO** verify EVERY school name, county name, state name in lists
- **DO** verify EVERY tuition figure, deadline, duration

"Key claims verified" is NOT the same as "file verified."

---

## Data Model

### Layer 1: State Residency
Legal determination of which state(s) you qualify for

### Layer 2: School Preferences
Which schools favor your profile beyond just residency (regional preferences, ties, partnerships)

---

## File Structure

```
policies/
├── index.yaml          # Compact summary for quick lookups
├── schema.yaml         # Field definitions
├── states/{state}/
│   ├── residency.yaml  # State residency rules
│   └── schools.yaml    # School-specific preferences
└── regional_programs/  # Multi-state partnerships (WWAMI, etc.)
```

---

## Agent Behavior

- Track ALL potentially relevant states dynamically
- Proactively identify if target state is weak
- Always cite specific statute/policy sections
- Provide strengthening advice for borderline claims

---

## Quality Checks

Before finalizing research:
- [ ] All claims have source citations
- [ ] Full visa eligibility lists (not partial)
- [ ] Admission vs tuition eligibility distinguished
- [ ] Programs explained with how/when to access
- [ ] Edge cases addressed
- [ ] Common applicant questions answered
