---
name: elsevier-cas-format
description: Use this skill whenever writing or editing LaTeX content destined for an Elsevier journal that uses the CAS template (cas-sc.cls or cas-dc.cls). Covers frontmatter macros, author/affiliation block, abstract, highlights, keywords, figures, tables, references with cas-model2-names.bst, biography blocks, and the \printcredits directive. Engineering Failure Analysis manuscripts in this repository use the cas-dc (double-column) variant.
---

# Elsevier CAS Template — Authoritative Conventions

This skill encodes the formatting rules for manuscripts using the `cas-dc.cls` (double-column) class from `els-cas-templates/`. The skeleton already exists at [els-cas-templates/cas-dc-template.tex](../../../els-cas-templates/cas-dc-template.tex); a working sample is at [els-cas-templates/cas-dc-sample.tex](../../../els-cas-templates/cas-dc-sample.tex).

## Document class declaration

```latex
\documentclass[a4paper,fleqn]{cas-dc}
```

Add `longmktitle` only if the frontmatter overflows one page:
```latex
\documentclass[a4paper,fleqn,longmktitle]{cas-dc}
```

## Frontmatter — required order

The CAS template expects these blocks **before** `\maketitle`, in this exact sequence:

1. `\shorttitle{}` and `\shortauthors{}` — running heads
2. `\title [mode = title]{}` — full title
3. `\tnotemark[1]` and `\tnotetext[1]{}` — title footnote (optional; omit both if not used)
4. `\author[N]{Name}[orcid=..., type=editor]` — one block per author
5. `\cormark[1]` placed **immediately after** the corresponding author's `\author` block
6. `\fnmark[1]` for footnote-marked authors
7. `\ead{email}` and `\ead[url]{}` — email and URL of that author
8. `\credit{...}` — CRediT contributions of that author
9. `\affiliation[N]{organization=, addressline=, city=, postcode=, state=, country=}`
10. `\cortext[1]{Corresponding author}` after all authors
11. `\fntext[1]{}` if footnotes were used
12. `\begin{abstract} ... \end{abstract}`
13. `\begin{graphicalabstract} \includegraphics{file} \end{graphicalabstract}` (optional)
14. `\begin{highlights} \item ... \end{highlights}`
15. `\begin{keywords} \sep keyword \sep keyword \end{keywords}` — note keywords are **\sep-separated**, NOT comma-separated
16. `\maketitle`

## Sections

```latex
\section{Section title}\label{sec:short-tag}
\subsection{Subsection title}\label{sec:short-tag-sub}
\subsubsection{...}\label{...}
```

Always use `\label{}` so cross-references work with `\ref{}` and `\autoref{}`.

## Figures

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\linewidth]{figs/fig1.pdf}
  \caption{Caption text. Use sentence case. End with a period.}\label{fig:short-tag}
\end{figure}
```

Two-column figures (spanning both columns):
```latex
\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{figs/fig1.pdf}
  \caption{...}\label{fig:wide-1}
\end{figure*}
```

**Image specs (Engineering Failure Analysis):** color/grayscale photos ≥ 300 dpi; line drawings ≥ 1000 dpi; preferred formats TIFF, EPS, PDF.

## Tables

CAS provides a `\tblwidth` macro for table width and `LL`/`LC`/`CC` column specs from `cas-common.sty`. Always use `booktabs` rules:

```latex
\begin{table}[t]
\caption{Caption text.}\label{tbl:short-tag}
\begin{tabular*}{\tblwidth}{@{}LCCC@{}}
\toprule
Header A & Header B & Header C & Header D \\
\midrule
Row 1A & Row 1B & Row 1C & Row 1D \\
Row 2A & Row 2B & Row 2C & Row 2D \\
\bottomrule
\end{tabular*}
\end{table}
```

For wide tables that span both columns, use `\begin{table*}[t]` and `\textwidth` instead of `\tblwidth`.

**Editable text only** — no images of tables, no scanned tables.

## References — bibliography style

The CAS template uses `cas-model2-names.bst` (author-year):

```latex
\bibliographystyle{cas-model2-names}
\bibliography{cas-refs}
```

For Engineering Failure Analysis, switch to numerical style at submission time:
```latex
%\bibliographystyle{model1-num-names}
\bibliographystyle{cas-model2-names}
```

The package `natbib` is loaded with `[authoryear,longnamesfirst]` in the template. To use numbered citations instead, change to `[numbers]`:
```latex
\usepackage[numbers]{natbib}
```

EFA uses **bracketed numbers** `[1]`, `[2]` in the final published version, so set `numbers` if you want the in-text citations to appear in that style.

## CRediT contributions

Each author's `\credit{}` block lists contributions from the official CRediT taxonomy (14 roles):
- Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Resources, Data curation, Writing - original draft, Writing - review & editing, Visualization, Supervision, Project administration, Funding acquisition

At the end of the document:
```latex
\printcredits
```
This auto-renders the consolidated CRediT statement.

## Biography blocks (optional)

```latex
\bio{photo-file}
Bio text here.
\endbio
```
Use the photo file basename without extension; the file goes in `figs/`.

## Compilation sequence

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## What NOT to do

- ❌ Do not load `geometry`, `fancyhdr`, or alternative font packages — `cas-dc.cls` already configures these and conflicts will break the layout.
- ❌ Do not use `\begin{table}\centering\begin{tabular}...` — the CAS template wants `\begin{tabular*}{\tblwidth}{...}` for proper column-aware widths.
- ❌ Do not put `\maketitle` before frontmatter macros — frontmatter blocks (`\title`, `\author`, abstract, highlights, keywords) must precede `\maketitle`.
- ❌ Do not separate keywords with commas — use `\sep`.
- ❌ Do not embed images of tables. Tables must be editable text.
- ❌ Do not include `\nocite{*}` in a final manuscript — it forces the bibliography to print every entry in the `.bib` file regardless of whether it was cited.

## Verification before submission

Run a `\listoftodos` check, ensure all `\label{}` are `\ref{}`'d at least once, confirm:
1. Title, author, affiliation, abstract, highlights, keywords all populated
2. CRediT statement present for every author
3. Corresponding author marked with `\cormark[1]` and `\cortext[1]`
4. Bibliography compiles without `???` references
5. All figures have captions; all tables have captions; both are referenced in text
