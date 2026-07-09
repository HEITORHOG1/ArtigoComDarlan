# Revisão simulada QREI (painel de 5 revisores + presidente) — 2026-07-09

> Manuscrito: `main.tex` (versão QREI). Método: llm-council no papel de revisores da QREI + examinadores de doutorado.
> **Veredito unânime: MAJOR REVISION.** Probabilidade de aceite: ~30–35% se apenas maquiar; **~60–65% com revisão diligente**.
> **Encaixa no perfil da QREI? SIM** (marginal, mas legitimado pelos precedentes BOBTA 2026 / Tang 2025 / Qian 2023).
> Estratégia central: **cortar o motor, promover o método.**

## CHECKLIST CONSOLIDADO DE MODIFICAÇÕES (priorizado)

### [BLOQUEADOR] — sem isto, rejeição no 2º round
1. **Ancorar ou rebaixar os limiares R≥1,20 e M≥1,5 mm.** Metodologia + Resultados. Elimina a circularidade de "reprovar contra a própria régua"; ou cita fonte externa, ou declara "project spec" e troca "reprovação" por *análise de sensibilidade do limiar*.
2. **Trocar "validação" por "verificação analítica / construct / plausibilidade" em todo o texto** + tabela verificação-vs-validação. Título, Abstract, cabeçalhos. O texto hoje declara empiria que não tem.
3. **Nomear o método (acrônimo) e enunciá-lo como framework transferível.** Título/Abstract/Intro.
4. **Abrir e enriquecer o Monte Carlo:** distribuições, correlações, convergência + incerteza de MODELO (dispersão de fadiga Cr-Si, derating térmico, carga dinâmica), não só tolerância de fabricação. Métodos + Resultados.
5. **Reenquadrar n=1 como proof-of-concept** com critério de transferibilidade + roadmap experimental. Intro + Limitações + roadmap.
6. **Declarar em UMA frase qual é o entregável:** o método (demonstrado no cabeçote), não um veredito sobre o cabeçote. Abstract + fim da Intro.

### [ALTO] — determinam se sobe para ~60-65%
7. **Reposicionar Abstract + Intro na contribuição de CONFIABILIDADE** (camada P[fail] de estados de barreira), com headline quantitativo na 1ª frase do abstract.
8. **Promover o coil-bind marginal de 16,2% a resultado carro-chefe e REMOVER os disclaimers autodepreciativos** ("does not claim a new general method"). Abstract/Resultados/Discussão.
9. **Formalizar os limiares de status P[fail] (at-risk/marginal/active) + sensibilidade aos cortes.** Métodos (nova subseção).
10. **Contraste FMEA/RPN vs P[fail] substantivo e quantitativo (vs Tang 2025).** Discussão/Related work.
11. **Elevar o benchmark de construct-validity a tabela com métrica de concordância** vs os 4 casos. Resultados/Discussão.
12. **Related work vs precedentes QREI (BOBTA/Tang/Qian)** — desarma o risco de desk-reject. Intro/Related work.
13. **Recast da varredura 6–12k rpm:** (a) robustez do método sobre ≥2 configurações e (b) envelope de operação fechado (surge ~9.800 / R≥1,20 ~10.500 / perda de contato ~11.500 rpm) como figura central.
14. **Expandir referências de 24 para ~35** (barrier-based reliability, surge de mola de válvula, MC em fadiga).
15. **Graphical abstract.** Artefato de submissão.
16. **Diferenciar o método de LOPA / barrier-quantification.** Related work/Discussão.

### [MÉDIO] — qualidade e legibilidade
17. **Enxugar de 37 para ~25-28 páginas:** mover ~60% do dimensionamento mecânico (inclusive a álgebra de f_n) para apêndice/suplementar.
18. **Glossário/nomenclatura** (coil-bind, surge, Goodman, Wahl, cam harmonics). Front matter.
19. **Figura-resumo do fluxo do método** (BowTie → indicadores → Monte Carlo → RPN). Métodos.
20. **Depositar script + dados no Zenodo com DOI + Data Availability Statement.**
21. **Passada de inglês britânico consistente.**

### [BAIXO] — housekeeping de submissão
22. **Alinhar keywords ao método nomeado.**
23. **Sugerir revisores + confirmar roteamento (Editor-in-Chief/associate editor).**
24. **Declaração de novidade / template NJD para pós-aceite.**

## Divergências notáveis do painel
- **Probabilidade:** pessimistas (Cético, Olhar Externo) ~30-35% veem lacuna estrutural de validação; otimistas (Expansionista, Executor) ~60-70% veem núcleo sólido mal-embalado. Reconciliação: ambos certos — depende de o autor executar de verdade vs maquiar.
- **"Reprova em 2 barreiras" = bug ou feature?** Vira *feature* (prova de que a triagem funciona) SE, e só se, os limiares forem ancorados externamente (item 1). Sem isso, colapsa em circularidade.
- **Expandir vs enxugar:** não é contradição — mesma cirurgia: cortar gordura mecânica, implantar músculo de confiabilidade.
