# Manuscrito LaTeX — BowTie Valve-Train Paper

**Título:** *BowTie Risk Analysis of the Valve Train in a High-Performance VW AP 1.8 Cylinder Head Operating at 10,000 rpm*
**Periódico-alvo:** Proceedings of the IMechE, Part D — Journal of Automobile Engineering (SAGE, Q2)
**Idioma:** British English
**Template (atual):** Elsevier `cas-dc.cls` (double column) — port para `sagej.cls` adiado para a fase pós-aceitação (IMechE Part D aceita PDF em qualquer formato razoável na submissão inicial).
**Periódico anterior (descartado):** Engineering Failure Analysis (Elsevier, Q1) — descartado em 2026-04-30 após parecer do orientador identificar incompatibilidade de escopo (revista de análise forense vs. trabalho prospectivo). Ver `memory/target_journal_switch.md`.

## Estrutura de arquivos

```text
artigo/
├── main.tex                       # frontmatter + \input das 6 seções
├── secoes/
│   ├── 01_introduction.tex        # ✅ prosa completa
│   ├── 02_background.tex          # ✅ prosa completa, 8 refs reais citadas
│   ├── 03_methodology.tex         # ✅ Tab. 1 (premissas) + Tab. 2 (indicadores)
│   ├── 04_results.tex             # ✅ Tab. 3 + 4 figuras + barreira crítica nomeada
│   ├── 05_discussion.tex          # ✅ Tab. 4 (BowTie vs FMEA) + limitações
│   └── 06_conclusion.tex          # ✅ síntese final
├── figs/
│   ├── fig1_bowtie.tex            # diagrama BowTie em TikZ
│   ├── fig2_lift.tex              # perfil de levante (pgfplots)
│   ├── fig3_fn.tex                # f_n vs harmônicas do came (pgfplots)
│   └── fig4_tornado.tex           # tornado plot (TikZ)
├── refs.bib                       # 14 entradas reais, todas com DOI
├── highlights.txt                 # 5 bullets ≤ 85 chars
├── cover-letter.txt               # esqueleto endereçado ao Editor
├── cas-dc.cls                     # cópia local para compilação
├── cas-common.sty                 # idem
├── cas-model2-names.bst           # idem (estilo bib author-year)
└── thumbnails/                    # ícones sociais do template (cópia)
```

## Compilação

```bash
cd artigo
pdflatex main
bibtex   main
pdflatex main
pdflatex main
```

O resultado é `main.pdf`. Avisos de `???` em referências indicam entradas `.bib` ainda não completadas (esperado nesta fase).

## Status por seção

| Seção | Estado | O que falta |
| --- | --- | --- |
| Frontmatter (main.tex) | ✅ Pronto | Confirmar ORCID dos dois autores |
| Abstract | ✅ Draft em prosa | Revisão final pelo orientador |
| Highlights | ✅ 5 bullets ≤ 85 chars | Aprovação do orientador |
| Keywords | ✅ 5 escolhidas | Aprovação do orientador |
| 1. Introduction | ✅ Prosa completa | Revisão pelo orientador |
| 2. Background | ✅ Prosa completa, 8 refs reais citadas | Revisão pelo orientador |
| 3. Methodology | ✅ **Tab. 1 com 22 linhas reais; Tab. 2 com 5 indicadores** | Revisão pelo orientador |
| 4. Results | ✅ **Prosa + Tab. 3 com 11 indicadores quantificados** | Revisão pelo orientador |
| 5. Discussion | ✅ **Barreira crítica nomeada (coil-bind externa)** | Revisão pelo orientador |
| 6. Conclusion | ✅ **Conclusão final com achados concretos** | Revisão pelo orientador |
| Figuras | ✅ **4 figuras nativas em TikZ/pgfplots** | — |
| Bibliografia | ✅ 14 refs reais (Crossref-verified) | — |
| Cover letter | ⚠ Esqueleto | Sugerir 3–5 revisores |
| Compilação | ✅ **Compila limpo, 10 páginas** | — |

## Achado central do artigo

**Barreira crítica identificada:** *outer-spring coil-bind margin*
($M_\mathrm{out} = 0{,}78$ mm vs. critério $M \geq 1{,}5$ mm).
**Concern secundário:** outer-spring natural frequency
($f_{n,\mathrm{out}}/f_\mathrm{cam}^{\max} = 3{,}81$ vs. regra de ouro $\geq 4$).
Ambos apontam para a **mola externa** como componente limitante do trem de válvulas a 10.000 rpm — exatamente o que a nota de dimensionamento do AP 1.8 já indicava como ajuste necessário.

## 4 figuras criadas (todas vetoriais, nativas LaTeX)

| Figura | Conteúdo | Tecnologia |
| --- | --- | --- |
| **Fig. 1** | Diagrama BowTie completo (T1–T6, P1–P5, evento topo, M1–M5, C1–C5, com setas de causalidade) | TikZ |
| **Fig. 2** | Tornado plot mostrando $M_\mathrm{out}$ em vermelho como única barreira que falha sob perturbação | TikZ |
| **Fig. 3** | Perfil de levante da válvula vs. ângulo de manivela com marcação dos pontos críticos $a_{\max,+}$ e $a_{\max,-}$ | pgfplots |
| **Fig. 4** | Frequências naturais das molas vs. primeiras 6 harmônicas do came no range de rotação | pgfplots |

## 4 tabelas com dados reais extraídos dos PDFs auxiliares

| Tabela | Conteúdo | Fonte dos dados |
| --- | --- | --- |
| **Tab. 1** | 22 linhas de premissas: motor (bore/stroke/displacement/4 cyl), regime (10.000 rpm), válvulas (Ti-6Al-4V, INCONEL 751), came (a_+, a_−, L_+, L_−), massas equivalentes, montagem de molas duplas Cr-Si | dissertacao.pdf §1.1, §3.2 + ambos os PDFs auxiliares |
| **Tab. 2** | 5 indicadores quantitativos com fórmula e critério de passa | Heywood + Shigley + AP 1.8 spec |
| **Tab. 3** | 11 resultados quantificados (4 razões dinâmicas, 2 freq. naturais, 2 coil-bind, 2 fadigas, 1 hot clearance) | Calculados dos PDFs |
| **Tab. 4** | Comparação BowTie vs. FMEA/RPN em 6 critérios | Argumento do artigo |

## Bibliografia consolidada (14 entradas)

**4 papers de valve-train / engine-component failure (validação qualitativa em §4.5):**

1. Vélez Godiño et al. 2019 — overhead valve train urban buses — *Engineering Failure Analysis* — DOI 10.1016/j.engfailanal.2018.11.003
2. Soffritti et al. 2018 — worn valve train four-cylinder diesel — *Engineering Failure Analysis* — DOI 10.1016/j.engfailanal.2018.06.022
3. Xing et al. 2021 — environment-assisted cracking high-strength valve springs — *Engineering Failure Analysis* — DOI 10.1016/j.engfailanal.2021.105466
4. Zhao et al. 2023 — V6 camshaft bearings lubrication — *Engineering Failure Analysis* — DOI 10.1016/j.engfailanal.2023.107329

**4 papers de outros periódicos (BowTie + spring fatigue):**

1. de Ruijter & Guldenmund 2016 — BowTie review — Safety Science — DOI 10.1016/j.ssci.2016.03.001
2. Khakzad et al. 2013 — BowTie + Bayesian network — PSEP — DOI 10.1016/j.psep.2012.01.005
3. Aust & Pons 2019 — BowTie aircraft engine borescope — Aerospace — DOI 10.3390/aerospace6100110
4. Ko et al. 2022 — surface flaws on valve-spring fatigue life — Scientific Reports — DOI 10.1038/s41598-022-25597-1

**5 textbooks âncora + 1 dissertação:** Heywood, Stone, Taylor, Shigley, Heisler, Porto.

Todas as 14 entradas foram **verificadas via Crossref API** antes de ir para o `refs.bib`. Nenhuma inventada.

## Próximos passos sugeridos

Itens concluídos no rework de 2026-04-30 (após parecer do orientador):

- ✅ Abstract, Introduction §1.5 e Conclusion reescritos como "design-stage reliability assessment" (não "failure analysis")
- ✅ Tabela comparativa em §2.3 mapeando cada um dos 4 case studies para barreira BowTie e indicador
- ✅ Nova §4.5 com validação qualitativa contra os 4 case studies (Xing → indicador determinístico; Vélez Godiño → mitigativo; Soffritti → qualitativo / motiva P6; Zhao → fora de escopo / motiva barreira de lubrificação)
- ✅ §5.3 Limitations reordenada: "no experimental validation" como item #1, com plano quantificado (banco de mola 50–600 Hz, motored-engine sweep, fadiga inner-spring n≥5, 600–800 h)
- ✅ §6 Conclusion estendida com Validation Roadmap explícito (3 estágios + critérios de aceitação)
- ✅ Cover letter reescrita para IMechE Part D
- ✅ Highlights, Data Availability e cabeçalho de `main.tex` atualizados

Pendentes pré-submissão:

1. **Leitura conjunta com o orientador** do draft atualizado antes de submeter
2. **Confirmar ORCIDs** dos coautores (placeholders nos comentários do `main.tex`)
3. **Revisão BrE final**: rodar busca por padrões AmE (`optimization`, `behavior`, `analyze`, `modeling`) e converter para BrE
4. **Verificar ângulo** das 5 sugestões de revisores na cover letter com o orientador

Pendentes pós-aceitação (não bloqueiam submissão):

1. **Port de template** `cas-dc.cls` → `sagej.cls` (SAGE) — IMechE Part D aceita qualquer formato razoável na submissão inicial; port só vira necessário se o editor pedir
2. **Estilo bibliográfico** Harvard SAGE (mantém author-year, mas `cas-model2-names.bst` precisa virar `SageH.bst`)
3. **Bloco de Highlights** pode precisar virar "Practical Applications" no formato SAGE (verificar instruções da revista no momento da revisão)

## Política do projeto

Esta pasta é governada pelas **3 skills locais** em [`.claude/skills/`](../.claude/skills/):

- `bowtie-paper-darlan` — política do artigo (zero invenção, escopo travado)
- `engineering-failure-analysis` — regras da revista
- `elsevier-cas-format` — convenções do template

A regra mais importante: **zero invenção**. Se um número não está nos PDFs ou em referência verificável, deixar `[VALUE FROM PDF X]` — não substituir por valor plausível.
