# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## Project Overview

This repository is the working directory for a **co-authored journal article with Darlan**. It is currently in the **source-material / pre-draft phase** — there is no LaTeX project, no codebase, and no `artigo/` build folder yet. Only the source PDFs and a `Codex/` notes folder are present.

**Article topic (from the source PDF):**
> *Avaliação Analítica dos Riscos de Detonação e Falha do Trem de Válvulas no Motor AP 1.8 com Aplicação da Metodologia BowTie, IoT e Inteligência Artificial*

(Analytical assessment of detonation and valve-train failure risks in the VW AP 1.8 engine, applying BowTie methodology, IoT monitoring, and AI for predictive support.)

**Domain:** automotive / high-performance internal combustion — NOT space systems. The two critical events under study are:
1. **Detonation (knock)** — abnormal combustion in the end-gas, driven by pressure/temperature/timing/compression-ratio interactions
2. **Valve-train failure at high RPM** — valve float, bounce, coil-bind proximity, spring-mass dynamics, vibration-induced degradation

**Methodological stack proposed by the source paper:**
- Analytical calculations (valve admission, springs at 10,000 RPM)
- BowTie diagrams (top event + threats + barriers + consequences)
- IoT sensing (rotation, temperature, vibration, pressure, combustion signatures)
- AI for pattern recognition / anomaly anticipation

## Current Repository Contents

```
g:/ArtigoComDarlan/
├── Avaliação Analítica dos Riscos de Detonação ... AP 1.pdf   # Source article draft
├── CALCULO DA VALVULA DE ADMISSÃO PARA 10.000RPM.pdf          # Analytical valve calc
├── CALCULO DAS MOLAS PARA 10.000RPM.pdf                       # Analytical spring calc
├── dissertacao.pdf                                            # Reference dissertation (~43 MB)
└── Codex/                                                    # Notes folder — see warning below
```

## ⚠ Stale Notes — `Codex/` folder

[Codex/AGENTS.md](Codex/AGENTS.md) and the other markdown files in [Codex/](Codex/) describe a **different project** (CubeSat FMEA with XGBoost + SHAP, co-authored with Celso, IEEE Access). They were copied from `ArtigoComCelso/` and **do not match the present topic** (engine knock + valve-train, with Darlan).

Do **not** treat those files as authoritative for this project. Either:
- Ignore them and rebuild the context fresh from the source PDFs, or
- Ask the user before reusing any IEEE-Access formatting rules from there.

The build command in [Codex/AGENTS.md:179](Codex/AGENTS.md#L179) (`cd "g:/ArtigoComCelso/artigo"`) confirms the wrong project — it points to a directory that doesn't exist here.

## Authoritative Source Material

When reasoning about this article, the source of truth is the PDFs in this directory — read them directly with the `Read` tool (it supports PDFs, max 20 pages per request). Do not invent data, equations, or references that are not in those PDFs or in materials the user supplies.

## Working Conventions

- **Article identity locked:** see [artigo-trem-valvulas-bowtie.md](artigo-trem-valvulas-bowtie.md) — the chosen paper is *BowTie Analysis of the Valve Train of a VW AP 1.8 Engine Operating at 10,000 rpm with a High-Performance Cylinder Head*, target journal **Engineering Failure Analysis** (Elsevier, Q1).
- **Manuscript language:** British English (consistent throughout — required by EFA).
- **LaTeX template:** Elsevier `cas-dc.cls` from [els-cas-templates/](els-cas-templates/).
- **Zero-invention policy:** never fabricate DOIs, reference entries, numerical results, or cite sources you have not actually read. If a required value is missing, leave a flagged placeholder and surface it to the user — do not substitute a plausible-looking number.
- **Title selection (Versão A vs B):** still pending orientador confirmation. Do not commit to one in the manuscript without explicit user instruction.
- **No LaTeX scaffolding yet:** the `artigo/` folder will only be created after the user explicitly says to start drafting. Do not pre-create it.

## Project-Local Skills

Three skills in [.Codex/skills/](.Codex/skills/) govern this project. They are auto-loaded by Codex when relevant:

- **[bowtie-paper-darlan](.Codex/skills/bowtie-paper-darlan/SKILL.md)** — project-specific rules (sources, scope, anti-fabrication, BowTie structure, forbidden expansions). **This is the highest-priority skill** for this project.
- **[engineering-failure-analysis](.Codex/skills/engineering-failure-analysis/SKILL.md)** — EFA submission rules (abstract limit, highlights format, declarations).
- **[elsevier-cas-format](.Codex/skills/elsevier-cas-format/SKILL.md)** — `cas-dc.cls` LaTeX conventions.

If the three skills disagree, `bowtie-paper-darlan` wins. See [.Codex/skills/README.md](.Codex/skills/README.md) for the full hierarchy.
