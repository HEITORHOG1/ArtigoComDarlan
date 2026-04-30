# Skills do Projeto — Artigo BowTie + Trem de Válvulas (Darlan)

Skills locais ao projeto, organizadas por escopo. Carregamento automático pelo Claude Code quando a descrição da skill casa com a tarefa.

## As três skills

| Skill | Quando usar | Escopo |
| --- | --- | --- |
| [`bowtie-paper-darlan`](bowtie-paper-darlan/SKILL.md) | Em **toda** edição/escrita do manuscrito deste projeto | Específica deste artigo |
| [`engineering-failure-analysis`](engineering-failure-analysis/SKILL.md) | Quando preparar/revisar para submissão à EFA | Genérica para EFA |
| [`elsevier-cas-format`](elsevier-cas-format/SKILL.md) | Quando editar o LaTeX usando `cas-dc.cls` | Genérica para Elsevier CAS |

## Hierarquia de precedência

Se as skills divergirem em uma regra:

1. `bowtie-paper-darlan` (mais específica) **vence**
2. `engineering-failure-analysis`
3. `elsevier-cas-format` (mais genérica)

Esta ordem está documentada também no topo da skill `bowtie-paper-darlan`.

## Resumo do que cada uma decide

### `bowtie-paper-darlan` — política do projeto

- Título escolhido (Versão A vs B)
- Autores e ordem
- Mapa de fontes autoritativas (qual PDF respalda qual claim)
- **Disciplina anti-fabricação** (zero invenção de dados, DOIs, etc.)
- Estrutura BowTie acordada (top event, ameaças, barreiras, consequências)
- Camada quantitativa (fórmulas e critérios de pass)
- Estrutura do artigo travada (6 seções)
- Escopos **proibidos** (knock, LSPI, IoT/IA, otimização — pertencem a outros títulos)
- Highlights, keywords, CRediT pré-alocados
- Localização final do projeto LaTeX (`artigo/`)

### `engineering-failure-analysis` — regras da revista

- Tipo de artigo (Full-Length Research)
- Limite do abstract (≤ 250 palavras)
- Highlights: 3–5 bullets, ≤ 85 caracteres cada
- Keywords: 1–5
- Estilo de citação ([1] numerado)
- Especificações de figuras (300 dpi foto, 1000 dpi line drawing)
- Tabelas como texto editável
- Idioma BrE consistente
- Declarações obrigatórias na submissão
- Sistema de submissão (Editorial Manager) e timeline esperada

### `elsevier-cas-format` — convenções do template

- Declaração `\documentclass[a4paper,fleqn]{cas-dc}`
- Ordem do frontmatter (título → autores → afiliação → abstract → highlights → keywords → maketitle)
- Macros específicas: `\cormark`, `\fnmark`, `\credit`, `\affiliation`
- `\sep` para separar keywords (NÃO vírgula)
- `\begin{tabular*}{\tblwidth}{...}` com booktabs
- `\bibliographystyle{cas-model2-names}`
- `\printcredits` no fim
- Sequência de compilação (`pdflatex → bibtex → pdflatex × 2`)
- Lista do que NÃO fazer (não carregar `geometry`, `fancyhdr`, etc.)

## O que essas skills NÃO fazem

- Não escrevem o artigo automaticamente — apenas governam **como** ele será escrito
- Não decidem o conteúdo científico — esse é seu trabalho com o orientador
- Não substituem leitura crítica do próprio orientador antes da submissão

## Atualização das skills

Se o escopo do artigo mudar (ex.: orientador pedir para incluir um cálculo CFD), atualize **`bowtie-paper-darlan`** primeiro. As outras duas raramente precisam mudar — elas são reflexo do template e da revista, não do projeto.
