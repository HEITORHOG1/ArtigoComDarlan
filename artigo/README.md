# Manuscrito LaTeX — BowTie Valve-Train Paper

**Título:** *BowTie Risk Analysis of the Valve Train in a High-Performance VW AP 1.8 Cylinder Head Operating at 10,000 rpm*
**Periódico-alvo:** *Reliability Engineering & System Safety* (Elsevier, Q1) — submissão pelo portal <https://submit.elsevier.com/JRESS>
**Idioma:** British English
**Template:** Elsevier `elsarticle.cls` (preprint, 12pt) — single-column duplo-espaço para revisão; produção da Elsevier retipografa após aceite.
**Estilo bibliográfico:** `elsarticle-num-names` (numerada com nome dos autores em `\citet`).

## Histórico de revistas (apenas referência)

- **2026-05-25 — alvo atual: RESS** (Reliability Engineering & System Safety). Port `cas-dc → elsarticle` concluído nesta data.
- 2026-04-30 — IMechE Part D (SAGE, Q2) — submetida e rejeitada.
- Pré-2026-04-30 — Engineering Failure Analysis (Elsevier, Q1) — descartada por incompatibilidade de escopo.

## Estrutura de arquivos

```text
artigo/
├── main.tex                       # frontmatter elsarticle + \input das 6 seções
├── secoes/                        # corpo do artigo (template-agnóstico)
│   ├── 01_introduction.tex
│   ├── 02_background.tex
│   ├── 03_methodology.tex
│   ├── 04_results.tex
│   ├── 05_discussion.tex
│   └── 06_conclusion.tex
├── figs/                          # 4 figuras nativas em TikZ/pgfplots
├── refs.bib                       # 18 entradas verificadas (Crossref)
├── highlights.txt                 # 5 bullets ≤ 85 chars
├── cover-letter.txt               # ⚠ ENDEREÇADO À IMECHE — precisa reescrever para RESS
├── main_cas-dc_backup.pdf         # PDF de referência da versão cas-dc anterior
├── thumbnails/                    # ícones sociais (legado cas-dc; manter por enquanto)
└── legacy/
    ├── cas-dc/                    # template antigo (cas-common.sty, cas-dc.cls, cas-model2-names.bst)
    └── imeched/                   # pacote de submissão IMechE (main_anonymous.tex, refs_anonymous.bib, submission/)
```

## Compilação

```bash
cd artigo
pdflatex main
bibtex   main
pdflatex main
pdflatex main
```

O resultado é `main.pdf`. `elsarticle.cls` e `elsarticle-num-names.bst` são pacotes padrão do MiKTeX/TeX Live — não precisam ser copiados localmente.

## Requisitos RESS (verificados no Guide for Authors em 2026-05-25)

| Requisito | Valor RESS | Estado atual |
| --- | --- | --- |
| Limite de palavras (manuscrito) | 13.000 | A verificar após port (PDF tem 13.998 incluindo bibliografia/captions) |
| Highlights | bullets curtos | ✅ 5 bullets ≤ 85 chars |
| Keywords | 1 a 7 | ✅ 5 |
| CRediT | recomendado | ✅ seção manual no main.tex |
| Corresponding authors | **único** | ✅ apenas Darlan |
| Estilo bibliográfico | numerado | ✅ `elsarticle-num-names` |
| Tipo de blind review | (não confirmado pelo Guide) | Default: single-blind. Material double-blind movido para `legacy/imeched/`. |
| Declarations | Competing interests, Funding, Data availability | ✅ todas presentes |

## Próximos passos pré-submissão

1. **Reescrever `cover-letter.txt`** para RESS (atualmente endereçada à IMechE Part D).
2. **Selecionar 3–5 suggested reviewers** apropriados ao perfil RESS (a lista da IMechE pode ser parcialmente reaproveitada — Soffritti, Vélez Godiño, Khan, Guldenmund, Aust são todos publicados em RESS-adjacentes).
3. **Contar palavras do corpo** (excluindo abstract/highlights/refs/captions) para confirmar ≤ 13.000.
4. **Confirmar com Darlan** se single-blind é aceitável (default RESS).
5. **Revisão final** dos 4 coautores antes do upload no portal JRESS.

## Política do projeto

- **Zero invenção:** nenhum DOI, número ou citação foi fabricado. Tudo verificável nos PDFs-fonte ou em entradas Crossref.
- **secoes/*.tex são template-agnósticas** — o port para elsarticle só alterou o frontmatter de `main.tex` e o cabeçalho `\begin{table*}[...]` (5 ocorrências de sintaxe cas-dc convertidas para LaTeX padrão).
- As macros CAS `L`, `C`, `R`, `\tblwidth` foram **replicadas no preâmbulo de `main.tex`** para que as tabelas existentes funcionem sem reescrita.

Skills locais que governam este projeto: `.claude/skills/bowtie-paper-darlan`, `.claude/skills/engineering-failure-analysis` (regras Elsevier gerais valem em parte para RESS), `.claude/skills/elsevier-cas-format` (agora apenas para `legacy/cas-dc/`).
