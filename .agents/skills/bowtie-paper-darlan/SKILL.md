---
name: bowtie-paper-darlan
description: Use this skill when writing or editing the manuscript "BowTie analysis of the valve train of a VW AP 1.8 engine operating at 10,000 rpm with a high-performance cylinder head", co-authored by Darlan Costa Porto. This skill encodes (a) the zero-invention discipline that prevents fabricated data/refs/DOIs, (b) the source-material map (which dissertation sections and PDFs are authoritative for which claims), (c) the agreed BowTie methodology and the quantitative coupling layer, and (d) the article structure, scope boundaries, and forbidden expansions.
---

# BowTie Paper (Darlan) — Project-Specific Rules

This skill governs **only** the manuscript described in [artigo-trem-valvulas-bowtie.md](../../../artigo-trem-valvulas-bowtie.md). It complements two other skills:

- `elsevier-cas-format` — LaTeX template conventions
- `engineering-failure-analysis` — journal submission rules

If those three skills disagree, **this one wins** (project-specific overrides generic).

## Article identity

- **Working title (Versão A, recommended):** *BowTie Analysis of the Valve Train of a VW AP 1.8 Engine Operating at 10,000 rpm with a High-Performance Cylinder Head*
- **Authors (in order):** Darlan Costa Porto (corresponding); Prof. Dr. José Cristiano Pereira (orientador)
- **Affiliation:** Centro de Engenharia e Computação, Programa de Mestrado em Sistemas de Engenharia, Universidade Católica de Petrópolis, Petrópolis, RJ, Brazil
- **Target journal:** Engineering Failure Analysis (Elsevier, Q1, IF 6.22)
- **Language:** British English, consistent throughout
- **Length target:** 8–12 pages, cas-dc double-column

## Source material — authoritative map

When writing any factual claim, it MUST be traceable to one of these sources. Cite the source in this skill, then in the manuscript cite the formal academic reference (book/paper).

| Claim domain | Authoritative source |
| --- | --- |
| AP 1.8 engine geometry (bore 81.0 mm, stroke 86.4 mm, displacement 1781 cm³, 4-cyl) | `dissertacao.pdf` § 1.1 (Contextualização) |
| Operating regime (10,000 rpm) | `dissertacao.pdf` § 3.2.6 (Premissas operacionais) |
| Valve-train mechanical premises | `dissertacao.pdf` § 2.3.7, § 3.2.7 |
| Compression ratio 14.5:1 (mention, not central) | `dissertacao.pdf` § 2.4.5 |
| Pent-roof chamber, asymmetric quench, GDI, iridium spark | `dissertacao.pdf` § 2.4.1–2.4.4 (mention only as cylinder head context) |
| Valve dimensioning calculations | `CALCULO DA VALVULA DE ADMISSÃO PARA 10.000RPM.pdf` |
| Valve-spring calculations (stiffness, natural frequency, coil-bind margin, fatigue) | `CALCULO DAS MOLAS PARA 10.000RPM.pdf` |
| Existing draft of the BowTie diagram | `Avaliação Analítica dos Riscos de Detonação e Falha do Trem de Válvulas no Motor AP 1.8 …BowTie, IoT e IA.pdf` (use as starting point only — restructure for the EFA paper) |
| Anchor textbook citations | Heywood (1988), Stone (2012), Taylor (1985) — verify edition/DOI before citing |

## ZERO-INVENTION DISCIPLINE (hard rule)

This article will be submitted to a peer-reviewed Q1 journal. Fabrication is unrecoverable.

❌ **Never invent:**
- Numerical values for spring stiffness, natural frequencies, masses, lift profiles, fatigue limits
- DOI numbers, ISBN numbers, page ranges
- Author names of cited works
- Dates of publication
- Quantitative results (R², MAPE, percent improvements)
- Experimental setups that do not exist

✅ **Allowed:**
- Numerical values that are **calculated** from formulas using inputs declared in the source PDFs (and the calculation must be reproducible from those inputs)
- Citations to real, verified references (DOI checked against Crossref before inclusion)
- Statements like "no experimental validation has been performed in this study; bench-test validation is left for future work"

If a claim is needed but the source data is missing, mark it `[TO BE COMPUTED FROM PDF X]` or `[REFERENCE PENDING — VERIFY BEFORE SUBMISSION]` and flag it in the chat. **Never substitute a plausible-looking number.**

## BowTie methodology — agreed structure

### Top event
**Loss of follower contact between valve and cam** (valve float / bounce / approach to coil bind).

### Threats (left side of bow)
1. Insufficient spring stiffness for the inertial regime
2. Excessive moving mass (valve + retainer + part of spring)
3. Aggressive cam profile (high acceleration peak)
4. Spring heating in operation (loss of effective stiffness)
5. Out-of-tolerance thermal clearance
6. Resonance between cam harmonics and spring natural frequency

### Preventive barriers
1. Dynamic dimensioning: `f_n_spring / f_cam_max ≥ 4`
2. Dual / nested springs (redundancy)
3. Low-mass tappets (lifters)
4. High-fatigue-resistance materials (Cr–Si, Cr–V steels)
5. Modal analysis and dynamometer validation

### Consequences (right side of bow)
1. Valve-piston collision
2. Catastrophic cylinder-head failure
3. Immediate loss of compression
4. Oil contamination by debris
5. Unscheduled engine shutdown

### Mitigative barriers
1. Electronic rev limiter
2. Cam-position sensor
3. Operating envelope defined at design stage
4. Torque / fuel cut-off
5. Predictive maintenance via vibration signals

## Quantitative layer — formulas to be filled from the PDFs

| Indicator | Formula | Pass criterion | Source for inputs |
| --- | --- | --- | --- |
| Spring natural frequency | `f_n = (1/2π)·√(k_eff / m_eff)` | `f_n / f_cam_max ≥ 4` | `CALCULO DAS MOLAS…` |
| Coil-bind margin | `δ_avail = L_compressed_total − L_max_cam` | `δ ≥ 0.15 · δ_total` | `CALCULO DAS MOLAS…` |
| Spring fatigue | shear stress amplitude vs S–N limit | `σ_max / σ_lim ≤ 0.5` (FoS = 2) | `CALCULO DAS MOLAS…` + material datasheet |
| Inertia × spring preload | `m·a_peak ≤ F_preload` at TDC | margin > 0 | `CALCULO DA VALVULA…` |
| Hot-clearance | clearance(T_max) ≥ 0 | always positive | derived from thermal-expansion data |

The **specific numbers** from the AP 1.8 calculations PDFs must be extracted into Table 2 of the manuscript (Section 4). They must NOT be invented. Read the PDFs page by page when populating that table.

### Citing design-rule constants

Constants like `f_n / f_cam ≥ 4`, FoS = 2, 15% coil-bind margin are **literature conventions for SI engines at high rpm**. Cite the textbook source (Heywood § 6, Taylor § 14, Stone § 6) — do not present them as new contributions of this paper.

## Article structure (locked)

```
1. Introduction                              ~1.0 pg
2. Background                                ~1.5 pg
   2.1 Valve-train failure modes at high rpm
   2.2 BowTie methodology — concise review
   2.3 Related work
3. Methodology                               ~2.0 pg
   3.1 System under study
   3.2 Mechanical and operational premises
   3.3 Qualitative BowTie construction
   3.4 Quantitative layer
   3.5 Cross-check procedure
4. Results                                   ~3.0 pg
   4.1 BowTie diagram (Fig. 1)
   4.2 Quantitative barrier evaluation (Tables 1–3, Figs. 2–4)
   4.3 Critical-barrier identification
5. Discussion                                ~1.5 pg
   5.1 Implications for cylinder-head design
   5.2 Comparison with traditional FMEA / RPN
   5.3 Limitations
6. Conclusion                                ~0.5 pg
References                                   ~0.5 pg (15–25 refs)
```

## Forbidden scope expansions

These topics are explicitly **out of scope** for this paper. They belong to other titles in [titulos-artigo-bowtie.md](../../../titulos-artigo-bowtie.md):

- ❌ Knock / detonation analysis (that's Title 1)
- ❌ Pre-ignition / LSPI (that's Title 3)
- ❌ IoT + AI for monitoring (that's Title 4)
- ❌ Multi-objective optimisation under risk constraints (that's Title 5)
- ❌ CFD results or air-flow analysis (that's the dissertation core, not this article)
- ❌ Combustion-chamber geometry beyond a one-paragraph mention in § 3.1

If a reviewer asks for any of these, the response is: "this is an explicit scope choice; future work cites Title X as planned follow-up".

## Highlights — drafting rules

Each ≤ 85 chars. The five highlights must capture, in this order:

1. The risk being analysed (valve-train at 10,000 rpm)
2. The methodological tool (BowTie)
3. The quantitative novelty (coupling to dimensioning calculations)
4. The application domain (high-performance cylinder head, AP 1.8)
5. The most surprising single finding (e.g., which barrier is critical)

Verify each is ≤ 85 chars before submitting.

## Keyword bank (pick exactly 5)

From this pool, choose those most discoverable on Scopus:
- BowTie analysis
- Risk assessment
- Valve train
- Internal combustion engine
- High-speed engine
- Failure analysis
- Mechanical reliability
- Coil bind
- Valve float

Recommended choice: `BowTie analysis`, `Valve train`, `Risk assessment`, `Internal combustion engine`, `Mechanical reliability`.

## CRediT — pre-decided allocation (subject to orientador confirmation)

| Author | CRediT roles |
| --- | --- |
| Darlan Costa Porto | Conceptualization; Methodology; Formal analysis; Investigation; Visualization; Writing - original draft |
| José Cristiano Pereira | Conceptualization; Methodology; Supervision; Writing - review & editing; Project administration |

## Pre-submission checklist

Before invoking the submission system:

- [ ] Title — Versão A or Versão B confirmed by orientador
- [ ] Abstract ≤ 250 words (machine-counted)
- [ ] Highlights — 5 bullets, each ≤ 85 chars (machine-counted)
- [ ] Keywords — exactly 5, alphabetical order
- [ ] All numerical values traceable to PDF inputs (no `???`, no placeholders)
- [ ] All references have DOIs verified against Crossref
- [ ] BrE consistency checked (search for AmE patterns: optimization, behavior, analyzed)
- [ ] CRediT statement entered for every author
- [ ] Cover letter drafted with reviewer suggestions
- [ ] Data availability statement chosen
- [ ] Generative-AI disclosure drafted (must mention Codex if used in drafting)
- [ ] Conflict-of-interest statement drafted
- [ ] LaTeX compiles cleanly without `???` references or undefined labels
- [ ] PDF visually checked: caption fit, table fit, no orphan/widow issues
- [ ] Independent re-read by Darlan + orientador signs off

## Build location

The manuscript LaTeX project will live in `artigo/` (sibling of `els-cas-templates/`), with structure:

```
artigo/
├── main.tex                        # \documentclass{cas-dc}
├── secoes/
│   ├── 01_introduction.tex
│   ├── 02_background.tex
│   ├── 03_methodology.tex
│   ├── 04_results.tex
│   ├── 05_discussion.tex
│   └── 06_conclusion.tex
├── figs/
│   ├── fig1-bowtie.pdf
│   ├── fig2-lift.pdf
│   ├── fig3-fn.pdf
│   └── fig4-tornado.pdf
├── refs.bib
├── highlights.txt
└── cover-letter.txt
```

Do not create this folder until the orientador has confirmed Versão A vs B of the title and the go-ahead to start drafting.

## When in doubt — ask

Before doing any of the following, surface the question to the user:

- Adding a numerical value not present in the PDFs
- Citing a reference whose DOI you cannot verify
- Expanding scope beyond § 1–6 above
- Switching the title from the agreed version
- Submitting to a journal other than Engineering Failure Analysis
