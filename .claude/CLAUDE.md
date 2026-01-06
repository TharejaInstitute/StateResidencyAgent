# State Residency Agent - Project Guidelines

## File References

When referencing files in responses:
- Always use clickable markdown links: [filename](path/to/file)
- For specific lines: [filename:42](path/to/file#L42)
- For line ranges: [filename:10-25](path/to/file#L10-L25)
- Use relative paths from the project root

---

## The Confabulation Problem

**FUNDAMENTAL ERROR**: Claude can generate content that LOOKS like verified research (source tables, inline citations, direct quotes) but is actually confabulated from training data.

The format of well-cited research is easy to generate. But generating the FORMAT ≠ doing the WORK.

**When you write "[1]", that's not a record of verification - it's just text you generated.**

### The Core Rule

**You cannot produce research OUTPUT without doing research INPUT.**

A citation must be a RECORD of verification, not a FORMATTING ELEMENT.

### The Required Process

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

### The Correct Workflow

**WRONG**: "Let me write up the Texas residency research..." → generates full document

**RIGHT**: "Let me visit the TMDSAS website first..." → reads page → "I see on this page: [content]" → writes claim with citation → repeats for each source

---

## Policy Research Guidelines

### Citation Verification Rules

**CRITICAL: Never add citations without verification.**

1. **Before adding ANY citation** to a research file:
   - Actually visit the source URL
   - Verify the specific claim exists on that page
   - If WebFetch returns 403/blocked, use Playwright browser instead

2. **Citation format requirements**:
   - Every factual claim must have an inline citation — [#]
   - Direct quotes must include the exact text from the source
   - Citations must point to the SPECIFIC page where the information appears, not just a general website

3. **Multi-page sources**:
   - Many medical schools have information spread across multiple pages
   - Create separate source entries for each distinct URL
   - Don't assume information on one page exists on another

### Common Mistakes to Avoid

1. **Don't assume source content** - Just because a URL is labeled "State Eligibility" doesn't mean it contains class sizes, acceptance rates, or tuition info

2. **Don't conflate similar pages** - An "Admissions" page and an "Acceptance Statistics" page are different sources with different information

3. **Don't add citations while editing** - Read/verify sources FIRST, then update the file

4. **Verify before correcting** - When updating existing citations, re-verify the information actually appears at that source

### Browser Verification Process

When verifying sources:

1. Navigate to the URL using Playwright browser
2. Document what information is ACTUALLY on that page
3. Note what information is NOT on that page (but might have been assumed)
4. Identify any additional sources discovered during verification
5. Update the Sources Index with newly discovered sources
6. Correct any incorrect citations

### Source Index Format

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

### Research File Structure

Each state research file should have:
1. Sources Index table at the top
2. Every factual claim cited inline
3. Direct quotes for critical policy language
4. Schema section with source comments
5. Clear distinction between verified info vs. interpretations

---

## Medical School Research Specifics

### What to Research Per School

1. **Residency requirements** - Duration, what counts, exceptions
2. **Citizenship requirements** - US citizen, PR, DACA, international
3. **Documentation requirements** - What proof is needed
4. **Class composition** - % in-state vs out-of-state
5. **Special pathways** - Ties criteria, regional programs
6. **Deadlines** - Certification, application, enrollment

### Source Hierarchy

Prefer sources in this order:
1. Medical school's own admissions pages
2. State registrar/residency office pages
3. State legislature (RCW, statutes)
4. University system-wide policies

### Verification Checklist

Before marking a research file as verified:
- [ ] All URLs in Sources Index are valid (actually visit each one)
- [ ] Each citation points to content actually on that page
- [ ] Acceptance rates/class sizes from statistics page, not general admissions
- [ ] Citizenship requirements verified from admissions eligibility page
- [ ] Tuition figures verified from official tuition page
- [ ] Direct quotes match source text exactly
- [ ] DACA/international policies verified school-by-school from authoritative source
- [ ] File status updated with verification date

---

## Lessons Learned from Verification

These are all symptoms of the confabulation problem above:

### Examples of Confabulated Content

1. **Wyoming acceptance rates**: File showed ~40% when reality is 50.0%
   - Root cause: Generated plausible-sounding number without reading the statistics page

2. **Texas DACA schools**: File claimed 4 schools don't accept DACA; reality is 12
   - Root cause: Generated a partial list from training knowledge, didn't read TMDSAS page

3. **West Virginia tuition URL**: URL returned 404
   - Root cause: Generated a URL that "seemed right" without visiting it

4. **Direct quotes that weren't quotes**: Text in quotation marks that doesn't appear on source page
   - Root cause: Generated quote-formatted text based on what source "probably says"

### The Pattern

Every error follows the same form:
- Generated content that LOOKED verified (had citations, quotes, statistics)
- But was actually produced without reading the source
- The research FORMAT was there; the research PROCESS was not

### Verification Date Protocol

When updating research files after verification:
1. Update the status line to include verification date: `**Status**: Draft - verified via browser 2026-01-06`
2. Note any data that couldn't be verified
3. If a claim cannot be verified, either remove it or add explicit uncertainty marker

---

## CRITICAL: MSAR Is NOT a Valid Source

**MSAR (Medical School Admission Requirements) is NOT publicly available data.** Claude never had access to MSAR during training.

Any claims that appear to be from MSAR were confabulated from training data patterns, NOT from actual MSAR access. Common confabulated MSAR data includes:
- MCAT minimums/preferred scores by residency status
- Acceptance rates broken down by in-state vs out-of-state
- Specific county/regional preferences
- Detailed class composition percentages

**The Rule**: If data cannot be found on a medical school's public website, official policy PDFs, or federal data sources (IPEDS, AAMC public data), it should be marked as "not publicly available" rather than cited to a source that wasn't actually accessed.

---

## CRITICAL: Search for Official Policy Documents

Medical schools often have **official policy PDFs** that contain more detailed information than their public web pages. These are primary sources.

**Before removing claims as unverifiable:**
1. Search for official policy PDFs (e.g., "MD Admission Policy", "Admissions Policy Document")
2. Check the school's media/documents folders (e.g., `/media/` paths)
3. Look for LCME accreditation documents
4. Search for the specific claim with quotes + school name

**Example discovery**: Marshall's website Admissions Criteria page doesn't mention "bordering states", but their official Policy PDF (https://jcesom.marshall.edu/media/63690/2025_policydocument.pdf) explicitly states: "Bordering state residents (Kentucky, Maryland, Ohio, Pennsylvania, and Virginia) will be strongly considered."

**The workflow**:
1. Check website pages first
2. Search for official policy PDFs
3. If still not found, search web for school + specific claim
4. Only mark as "not publicly available" after exhaustive search

---

## CRITICAL: Verify EVERY Claim, Not Just Key Claims

**THIS IS A REPEATED MISTAKE. DO NOT SKIP THIS.**

When asked to verify research files:
- **DO NOT** verify only "key structural claims" or "main points"
- **DO** verify EVERY SINGLE claim that has a citation
- **DO** verify EVERY statistic, percentage, rate, figure
- **DO** verify EVERY visa type listed (F-1, J-1, H-1B, etc.)
- **DO** verify EVERY school name, county name, state name in lists
- **DO** verify EVERY tuition figure, deadline, duration

### Why This Matters

"Key claims verified" is NOT the same as "file verified." A research file with 50 claims where only 10 key claims were verified still has 40 potentially confabulated claims.

### The Checklist Approach

When verifying a file, create explicit checklist:
```
Claims to verify in [filename]:
- [ ] 366-day requirement — visit source [1]
- [ ] F-1 visa ineligible — visit source [2]
- [ ] Tuition $42,284 — visit source [5]
- [ ] 64% in-state composition — visit source [4]
... (EVERY claim with a citation)
```

Then systematically verify each one, documenting what you see.

### No Claim Is Too Small

Even if a claim seems obvious or minor:
- Verify it anyway
- Document what you see
- Mark it verified only after reading the source

**REMEMBER: The user has explicitly stated "EVERYTHING MUST BE VERIFIED" multiple times.**

---

## CRITICAL: Only Medical School Sources Are Valid

**For medical school residency research, ONLY use sources from actual medical schools.**

### Valid Sources
- Medical school admissions pages (e.g., UCSF School of Medicine, UCLA David Geffen)
- Medical school registrar pages
- State medical education coordinating boards (e.g., TMDSAS for Texas)
- University system medical education policies

### INVALID Sources
- **Undergraduate campus registrars** (e.g., UC Berkeley, UCLA main campus) - these schools may not have medical programs or may have different policies
- General university admissions pages (unless specifically for medical school)
- State financial aid commission pages (CSAC) - these are for undergrad aid, not medical school

### Why This Matters
UC Berkeley has NO medical school. Using UC Berkeley's registrar page as a source for medical school residency is WRONG because:
1. Their policies may differ from medical schools
2. They don't have medical students, so their immigration guidance doesn't apply
3. It creates false citations that cannot be verified at a medical school

### The Rule
**Every source cited in a medical school research file must be from:**
1. A medical school's own website, OR
2. A state/system policy document that explicitly applies to medical schools

**If you cannot find information on a medical school's website, note it as "needs medical school source" rather than citing an undergraduate institution.**
