# Submission package — Reliability Engineering & System Safety

**Portal:** <https://submit.elsevier.com/JRESS>
**Article type:** Research Paper
**Date prepared:** 25 May 2026

This folder contains the four PDFs (and their LaTeX sources) needed to
submit the manuscript *BowTie Risk Analysis of the Valve Train in a
High-Performance VW AP 1.8 Cylinder Head Operating at 10,000 rpm* to
*Reliability Engineering & System Safety* (Elsevier).

## Files in this package

| File | What it is | What to do with it in the portal |
| --- | --- | --- |
| [`01_cover_letter.pdf`](01_cover_letter.pdf) | Cover letter signed by the corresponding author. Addressed to the RESS Editor-in-Chief. Includes 5 suggested independent reviewers with affiliations and justifications. | Upload as "Cover Letter" |
| [`02_title_page.pdf`](02_title_page.pdf) | Title page with full author list, ORCIDs, e-mail addresses, affiliations, CRediT statement, and declarations (competing interests / funding / data availability). | Upload as "Title Page (with author details)" |
| [`03_highlights.pdf`](03_highlights.pdf) + [`03_highlights.txt`](03_highlights.txt) | Five highlights, each ≤ 85 characters. PDF for upload; `.txt` for pasting into the highlights text field if the portal requests it. | Upload PDF as "Highlights" — or paste the `.txt` content in the highlights text box |
| [`04_manuscript.pdf`](04_manuscript.pdf) | Full manuscript: frontmatter, 6 sections, 8 tables, 4 figures, CRediT, declarations, bibliography (23 references including 5 from RESS). Compiled from `../main.tex` with `elsarticle.cls` + `elsarticle-num-names.bst`. | Upload as "Manuscript" |

LaTeX sources (`.tex`) are kept alongside the PDFs so any wording edit
can be re-rendered with `pdflatex 0X_<file>.tex`.

## Suggested reviewers (verified in the cover letter)

All five are independent of UCP and PUC-Rio, and none has co-authored
work with the present authors. Each has a verifiable publication
history in *Reliability Engineering & System Safety* on a topic
relevant to the manuscript.

1. **Prof. Valerio Cozzani** — DICAM, University of Bologna, Italy.
   Safety barriers and process safety; multiple RESS papers including
   RESS 2021 DOI 10.1016/j.ress.2021.107634.

2. **Prof. Chia-Fen Chi** — National Taiwan University of Science and
   Technology (NTUST), Taipei. FMEA for vehicle recalls; RESS 2020
   DOI 10.1016/j.ress.2020.106929. Direct relevance to the BowTie-vs-FMEA
   comparison in our Discussion section.

3. **Prof. Saeed Khodaygan** — Department of Mechanical Engineering,
   Sharif University of Technology, Tehran, Iran. Bayesian reliability
   of mechanical assemblies; RESS 2021 DOI 10.1016/j.ress.2021.107748.
   Aligned with our Monte Carlo refinement under ASTM tolerances.

4. **Prof. Frank Guldenmund** — Section Safety and Security Science,
   Delft University of Technology, Netherlands. Co-author of the
   canonical BowTie review (Safety Science 2016) cited in our
   manuscript.

5. **Prof. Gabriele Landucci** — Department of Civil and Industrial
   Engineering, University of Pisa, Italy. Safety-barrier performance
   under domino-effect and Natech scenarios; multiple recent RESS
   papers including RESS 2020 DOI 10.1016/j.ress.2019.106597.

The cover letter notes that the final selection is at the editor's
discretion. The institutional e-mail addresses of each reviewer are
not embedded in this package — they should be looked up on each
researcher's institutional homepage at upload time.

## Upload checklist (in the JRESS portal)

1. Cover Letter → `01_cover_letter.pdf`
2. Title Page → `02_title_page.pdf`
3. Highlights → `03_highlights.pdf` (or paste `03_highlights.txt`)
4. Manuscript → `04_manuscript.pdf`
5. Article type: Research Paper
6. Suggested reviewers: copy the 5 names and affiliations from the
   cover letter into the portal's reviewer-suggestion form
7. Author contributions: already included in the title page (CRediT
   statement) and in the manuscript (just before the bibliography)
8. Declarations: already included in the title page and in the
   manuscript
9. Supplementary material: the Monte Carlo Python script reproducing
   Table 5 (mc-results) — to be added separately if/when the user
   provides the script file

## Pre-submission state checks

- Manuscript compiles cleanly: `cd .. && pdflatex main && bibtex main &&
  pdflatex main && pdflatex main` — zero error, zero undefined citation
  warnings.
- Manuscript word count (body + abstract): ≈ 13 000 words; within the
  RESS limit (manuscript ≤ 13 000 words).
- Page size: A4 (RESS/Elsevier expectation).
- Language: British English, consistent throughout.
- Bibliography: 24 entries, all Crossref-verified, all with working
  DOIs. Six of them are from RESS itself (five BowTie papers plus the
  Pillay & Wang 2003 RPN-critique), supporting the cover letter's
  case that the manuscript is methodologically aligned with the
  journal's BowTie tradition and grounded in the RPN-weakness
  literature.
- Section structure: 7 sections — Introduction, Background,
  Methodology, Results, Discussion, **Validation roadmap and future
  work**, Conclusion. The roadmap section was split out of the
  Conclusion in revision r2 to follow the structural separation
  expected by RESS reviewers (short final Conclusion, dedicated
  Future-work section).
- Highlights revised in r2 to ≤ 85 characters per bullet and to
  surface the two concurrent at-risk findings (outer-spring coil-bind
  margin 0.78 mm; inner-spring Goodman FoS 0.68 with 100 % MC
  failure) and the Monte Carlo refinement.

## How this package was assembled

1. `01_cover_letter.tex` was written from scratch for RESS, replacing
   the previous IMechE Part~D cover letter (archived in
   `../legacy/imeched/submission/`).
2. `02_title_page.tex` adapted the previous IMechE title page to name
   RESS as the target journal and Research Paper as the article type;
   author list, ORCIDs, affiliations and CRediT roles are unchanged.
3. `03_highlights.tex` mirrors the `\begin{highlights}` block inside
   the manuscript main file (`../main.tex`); the `.txt` companion is
   for portal text-field paste.
4. `04_manuscript.pdf` is a copy of `../main.pdf`, the build product
   of `../main.tex` using the `elsarticle.cls` template (preprint
   format, 12 pt, single column, A4) with
   `\bibliographystyle{elsarticle-num-names}`.

Single-blind review is the RESS default and was assumed during
package assembly; the manuscript file is **named** (not anonymous).
If RESS confirms a double-blind workflow during the upload, the
double-blind variant from the previous submission (in
`../legacy/imeched/`) can be re-rendered against the current
`refs_anonymous.bib` and the same `secoes/*.tex` body.
