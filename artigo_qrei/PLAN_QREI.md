# Plano de submissão à QREI (Quality and Reliability Engineering International, Wiley)

> **REVISADO pelo llm-council (2026-07-09).** A 1ª versão deste plano tratava um problema de
> SUBSTÂNCIA (3 rejeições por "n=1 / sem validação") como problema de FORMATAÇÃO. O conselho
> deu **NO-GO condicional** nela. Esta versão incorpora o veredito.

## Veredito do conselho (resumo)
- **Não portar o template Wiley NJD agora.** Wiley aceita formato livre na 1ª submissão; o
  template é trabalho de PÓS-aceite. (Cortar também preprint engrXiv por ora.)
- **Não fazer a "corroboração n=1→n=5".** Reaplicar o método aos 4 casos publicados é
  armadilha: os papers-fonte NÃO têm os inputs do Monte Carlo (taxas de mola, folgas, timing)
  → ou inventa (viola zero-invenção) ou fica vago. Manter o benchmark QUALITATIVO que o
  manuscrito já tem e rotulá-lo com honestidade como *face validity / plausibilidade
  estrutural* — NÃO "validação", NÃO "n=5". O paper assume-se como **estudo de caso único**.
- **Reframe "framework transferível" é arriscado:** prometer generalidade com 1 aplicação e
  zero validação ELEVA a barra de novidade. Reenquadrar com honestidade (case study + benchmark
  qualitativo), não superdimensionar.
- **Decisão de GÊNERO antes de revista:** avaliar submeter como paper de MÉTODO/tutorial (onde
  "sem bancada" é a categoria, não um defeito) vs research article de caso único.
- **Jogada mais barata e de maior valor:** *pre-submission inquiry* ao editor da QREI
  (título + abstract + os 3 DOIs-precedente) — confirma aderência de escopo antes de gastar horas.

## Bloqueador #1 (gate 0): pareceres de rejeição
- **NÃO temos as cartas de rejeição reais** (EFA / IMechE Part D / RESS) no repositório.
  O único documento é `../analise-critica-artigo.md` = autoanálise nossa (abr/2026, mirando EFA),
  não o parecer real de nenhum editor/revisor.
- **AÇÃO:** obter os pareceres reais — sobretudo o do **RESS** (mais recente e relevante).
  - Se RESS foi **desk-reject** (escopo, uma linha) → o problema é FIT → QREI + reframe honesto resolve.
  - Se RESS veio com **relatórios de revisor** citando "falta validação" → problema é SUBSTÂNCIA →
    pivô de gênero (método/software) ou aceitar o custo da bancada.

## Ordem de trabalho corrigida
1. **Reler os 3 pareceres reais** e tabular o motivo declarado de cada recusa. *(gate 0 — sem isto, nada avança)*
2. **Decidir o GÊNERO** (método/tutorial vs research article de caso único).
3. **Pre-submission inquiry** ao editor da QREI (email: título + abstract + 3 DOIs, perguntando aderência).
4. Só com resposta positiva: **reframe honesto** — case study + benchmark qualitativo; a cover letter
   responde DE FRENTE ao "n=1 / sem validação" (reconhece o limite, bancada como trabalho futuro
   declarado, defende por que a contribuição metodológica se sustenta mesmo assim).
5. **Conformidade editorial** (por último, ~30 min): abstract ≤230 palavras, refs numéricas [1]
   Vancouver/AMA, ≤5 keywords, tabelas após as referências.
6. **Template Wiley NJD:** só se/quando exigido pós-aceite (WileyNJD-v2; XeLaTeX + TeX Live 2022).

## Verdade desconfortável (registrada)
Se os 3 pareceres convergirem em "falta validação experimental", nenhuma reescrita honesta cura —
só (a) a campanha de bancada (600–800h) OU (b) o pivô de gênero. Uma 4ª submissão cosmética não é saída.

## Estrutura da pasta `artigo_qrei/` (quando for a hora)
```
artigo_qrei/
├── PLAN_QREI.md                 # este arquivo
├── presubmission_inquiry.txt    # email ao editor (passo 3) — a redigir
├── main.tex                     # manuscrito (formato livre 1ª submissão; NJD só pós-aceite)
├── refs.bib                     # reaproveitado de ../artigo/refs.bib
├── secoes/                      # copiado de ../artigo/secoes/ e adaptado (reframe honesto)
├── cover_letter_qrei.tex        # responde de frente ao "n=1/sem validação" + cita 3 DOIs
└── submission/                  # PDFs finais
```
