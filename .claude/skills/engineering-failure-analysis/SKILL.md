---
name: engineering-failure-analysis
description: Use this skill when preparing or revising a manuscript targeted at the Elsevier journal Engineering Failure Analysis (EFA). Encodes EFA-specific submission rules pulled from the journal's Guide for Authors (April 2026 consult): article types, abstract limit (≤250 words), highlights format (3–5 bullets ≤85 chars each), keyword limit (1–5), section numbering, language consistency, declarations required, reference style, figure/table specs, and the cover letter angle the journal expects.
---

# Engineering Failure Analysis — Submission Rules

Source: https://www.sciencedirect.com/journal/engineering-failure-analysis/publish/guide-for-authors (consulted April 2026).

## Article type

This manuscript is a **Research Paper** (research papers, short communications, and occasional reviews are accepted). Choose "Full Length Article" in the EM submission system.

## Length

No explicit page limit. Practical target: **8–12 typeset pages** in cas-dc double-column. Reviewers tend to be skeptical of papers below 6 pages (insufficient depth) or above 16 pages (insufficient focus).

## Abstract

- **Hard limit:** 250 words.
- **Self-contained:** no citations, no abbreviations defined elsewhere, no equations, no figure references.
- **Structure:** problem → approach → findings → implication, in 4–6 sentences.

## Highlights — exact format

Submitted as a **separate file**, not inside the manuscript.

- **3 to 5 bullet points**
- **Maximum 85 characters per bullet, including spaces**
- Each bullet captures a distinct contribution; do not paraphrase the abstract.

Verify length:
```python
for line in highlights:
    assert len(line) <= 85, f"Highlight too long ({len(line)} chars): {line}"
```

## Keywords

- **1 to 5 keywords**
- Avoid multi-word phrases joined by connectors (e.g., prefer "BowTie analysis" over "analysis of failure using BowTie methodology").
- Capitalize like sentence (first word only) unless a proper noun.

## Section numbering

- Numbered sections: 1, 1.1, 1.1.1.
- **Abstract is NOT numbered.**
- Acknowledgments, Funding, References — NOT numbered.
- Use brief headings on separate lines.

## Language

- American or British English. **Do not mix the two within a single manuscript.**
- This article: choose **British English** (UK spellings: optimisation, behaviour, analyse). Be consistent throughout.

## Reference style

- In-text: numbered in brackets `[1]`, `[2]`, `[1, 3]`, `[1–4]`.
- At submission, "no strict formatting requirements" — Elsevier reformats at proof stage.
- **Always include DOI** for journal articles when available.
- Order: by appearance in text.
- Aim for 15–30 references for a research paper at this length.

## Figures

- Submit as **separate files** (one per figure). Do not embed in the manuscript Word/LaTeX file alone — Elsevier's production needs the source files.
- Color or grayscale photos: **≥ 300 dpi**.
- Line drawings (vector preferred): **≥ 1000 dpi** if rasterised, otherwise EPS/PDF vector.
- Preferred formats: **TIFF, EPS, PDF**, MS Office.
- Each figure must be cited in text **before** it appears.
- Captions are full sentences with terminal periods.

## Tables

- **Editable text** only (no images of tables, no scanned tables).
- Caption above the table.
- Use simple horizontal rules (no vertical rules); booktabs `\toprule \midrule \bottomrule` is the convention.
- All tables must be cited in text before appearance.

## Graphical abstract (optional but recommended)

- Image dimensions: minimum 531 × 1328 pixels (5:2 portrait).
- Preferred formats: TIFF, EPS, PDF, or MS Office files.
- Single image — should communicate the work's core idea visually.
- For this manuscript: a simplified BowTie diagram is the natural graphical abstract.

## Required declarations at submission

All four are mandatory in the EM submission system:

1. **Declaration of competing interests** — even if "none", must be declared.
2. **Funding sources** — list each, with grant numbers if applicable. If unfunded, state so explicitly.
3. **Generative AI use** — if any AI tool was used in writing/research, disclose tool name and purpose. (We will need to declare honestly if Claude was used.)
4. **Research data availability statement** — choose one of: (a) data in supplementary, (b) data in repository (provide DOI), (c) data available on request, (d) data not generated (analytical study).
5. **CRediT author contributions** — full statement using the 14-role taxonomy. Required for every author.

## Cover letter — what EFA editors look for

A short letter (≤ 1 page) addressed to the Editor-in-Chief. Elements that improve handling:

1. **Article type** ("Full Length Research Article")
2. **One-sentence framing of the contribution** — what failure mode, what method, what's new
3. **Why EFA specifically** — link the methodology (BowTie) to the journal's published scope
4. **Confirmation of originality** — manuscript not under review elsewhere
5. **Suggested reviewers (3–5)** — names + emails + affiliations of researchers competent in BowTie / engine reliability / mechanical failure analysis. Do not suggest co-authors of the dissertation. Do not suggest researchers from the same institution.
6. **Excluded reviewers (optional)** — name 1–2 if there is a reasonable conflict.

## Submission system

Editorial Manager at https://www.editorialmanager.com/efa/

- Account is per-author; corresponding author submits.
- Manuscript file (.tex or .docx) — single editable file.
- Figures uploaded as separate files.
- Highlights uploaded as a **separate file** (often a `.docx` or `.txt`).
- Cover letter uploaded as a separate file.
- All declarations entered into EM forms (not in the manuscript).

## After submission — typical timeline

| Stage | Typical duration (Elsevier estimates) |
| --- | --- |
| With Editor (initial check) | 1–2 weeks |
| Under review | 6–12 weeks |
| First decision (revise / reject / accept) | up to 14 weeks total |
| Revision response | 1–2 months for major; 3–4 weeks for minor |
| Accept | usually 1 round, sometimes 2 |

## Common rejection reasons EFA cites

- Unclear or unsupported "novelty" claim
- BowTie/FMEA/FTA presented qualitatively without quantitative anchoring
- Failure mode not actually a failure (e.g., wear of a non-critical component)
- Insufficient comparison with prior literature on the same component
- Mixed AmE/BrE
- Reference list with broken DOIs or non-peer-reviewed sources
