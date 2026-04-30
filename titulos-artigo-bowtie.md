# 5 Títulos Propostos — Artigo de Mestrado (Dissertação Darlan + BowTie)

**Autor:** Darlan Costa Porto
**Programa:** Mestrado em Sistemas de Engenharia — UCP
**Dissertação-base:** *Otimização do Cabeçote do Motor AP 1.8 — Uma Análise Termodinâmica da Combustão e de Fluxo de Escoamento de Ar* (2026)
**Co-autoria sugerida:** orientador Prof. Dr. José Cristiano Pereira

---

## Princípio de seleção dos títulos

A dissertação é um trabalho de **otimização termodinâmica e fluidodinâmica** do cabeçote. O BowTie é uma ferramenta de **análise estruturada de risco** que organiza, em torno de um evento topo, as ameaças, as barreiras preventivas, as consequências e as barreiras mitigadoras. Os cinco títulos abaixo exploram interfaces diferentes entre os dois mundos — do mais focado num único modo de falha (Título 1 e 2) até o mais metodológico, que propõe integrar BowTie ao próprio processo de projeto (Título 5).

**Restrição editorial adotada:** todas as revistas sugeridas neste documento são **Q1 ou Q2 no Scimago (SJR)** e **gratuitas para o autor** — modelo de assinatura/híbrido publicando pela trilha *subscription*, sem APC obrigatório. Periódicos com APC obrigatório (ex.: IEEE Access, MDPI, Frontiers) **foram explicitamente descartados**. Ver a "Tabela mestre de revistas" no fim do documento para os critérios completos, valores de APC opcional, IF e SJR.

> **Nota sobre Qualis CAPES:** o sistema Qualis Periódicos foi descontinuado a partir do ciclo avaliativo 2025–2028 da CAPES — a nova avaliação migra para indicadores bibliométricos diretos do artigo (citações, SJR, JCR) combinados com critérios qualitativos. Como proxy estável e internacional, este documento usa **quartis Scimago (Q1/Q2)** e **fator de impacto JCR** atualizados para 2024 (publicados em 2025). A área CAPES de referência da dissertação é **Engenharias III** (Mecânica, Aeroespacial, Naval, Produção, Petróleo); para o Título 4 também se aplica **Engenharias IV** (IoT/IA).

---

## Título 1 — Knock como evento topo

**Análise BowTie da Detonação em Cabeçote de Alta Performance para Motor AP 1.8 a Etanol Operando com Taxa de Compressão 14,5:1**

### Por que este título
A taxa de compressão de 14,5:1 adotada na dissertação é justamente o ponto onde o **risco de knock** se torna sistemicamente crítico — o etanol é o que viabiliza essa TC, e o cabeçote (geometria de câmara, posição da vela, quench, GDI) é o que define a margem antidetonante real. A dissertação já contém todos os ingredientes físicos (critério de Livengood–Wu, faseamento da combustão, efeito do calor de vaporização do etanol, geometria do end-gas) — falta apenas reorganizar isso na **estrutura BowTie**, com ameaças de cada lado e barreiras quantificadas.

### Aproveitamento direto da dissertação
- Seções 2.4 (geometria da câmara em alta TC) e 2.8 (combustão anormal e knock)
- Seção 2.9 (etanol como combustível de referência)
- Modelo analítico do ciclo (Cap. 3.4) → fornece pressão e temperatura do end-gas
- CFD (Cap. 3.5) → fornece campo de temperatura, distribuição local de mistura, exposição do end-gas

### Estrutura BowTie proposta
- **Evento topo:** autoignição do end-gas (knock)
- **Ameaças:** alta TC; ponto de ignição avançado; carga térmica residual; mistura mal homogeneizada; falha do GDI; combustível fora de especificação
- **Barreiras preventivas:** geometria de câmara compacta; quench assimétrico; resfriamento evaporativo do etanol; controle do ângulo de ignição; vela de irídio; sensor de knock
- **Consequências:** perda de potência; pré-ignição em cascata (LSPI); dano à câmara/pistão; falha catastrófica
- **Barreiras mitigadoras:** retardo de ignição em malha fechada; corte de torque; enriquecimento; redução de carga

### Revistas-alvo do Título 1 (Q1, gratuitas — eixo combustão/etanol)

| Revista | Editora | Quartil 2024 | IF 2024 | APC obrigatório? | Aderência ao tema |
| --- | --- | --- | --- | --- | --- |
| **Fuel** | Elsevier (subscription) | Q1 | 8,78 | Não — gratuito por trilha *subscription* | Combustão de etanol, knock, motores SI — máxima aderência |
| **Combustion and Flame** | Elsevier (subscription) | Q1 | 7,13 | Não — gratuito por trilha *subscription* | Combustão fundamental, autoignição, end-gas |
| **Applied Thermal Engineering** | Elsevier (subscription) | Q1 | 7,86 | Não — gratuito por trilha *subscription* | Análise térmica do ciclo, perdas, transferência de calor |

Recomendação primária: **Fuel** (foco em combustível + combustão; o etanol é central na dissertação). Backup: *Combustion and Flame* se o texto enfatizar o critério de Livengood–Wu e a química de autoignição.

---

## Título 2 — Trem de válvulas como evento topo

**Avaliação de Risco do Trem de Válvulas em Motor AP 1.8 Otimizado para 10.000 rpm: uma Aplicação Integrada da Metodologia BowTie**

### Por que este título
A dissertação fixa **10.000 rpm** como regime de operação, e o item 2.3.7 já trata explicitamente dos requisitos mecânicos do trem de válvulas nesse regime. Os PDFs auxiliares já presentes no diretório (`CALCULO DA VALVULA DE ADMISSÃO PARA 10.000RPM.pdf` e `CALCULO DAS MOLAS PARA 10.000RPM.pdf`) **fornecem a base analítica pronta** para alimentar o BowTie. É o título com menor distância entre material disponível e artigo finalizado.

### Aproveitamento direto da dissertação
- Item 2.3.7 (requisitos mecânicos a 10.000 rpm)
- Premissas mecânicas e construtivas do trem de válvulas (item 3.2.7)
- PDFs auxiliares: cálculo da válvula de admissão e cálculo das molas

### Estrutura BowTie proposta
- **Evento topo:** perda de seguimento da válvula em relação ao came (valve float / bounce / aproximação ao coil bind)
- **Ameaças:** rigidez insuficiente da mola; massa móvel excessiva; perfil agressivo do came; aquecimento da mola; folga térmica fora de tolerância; ressonância na rotação operacional
- **Barreiras preventivas:** dimensionamento dinâmico (frequência natural × harmônica do came); molas duplas; tuchos de baixa massa; materiais com alta resistência à fadiga; análise modal
- **Consequências:** colisão válvula/pistão; falha catastrófica do cabeçote; queda imediata de compressão
- **Barreiras mitigadoras:** limitador eletrônico de rotação; sensor de posição do came; janela operacional definida em projeto

### Revistas-alvo do Título 2 (Q1/Q2, gratuitas — eixo falha mecânica/dinâmica)

| Revista | Editora | Quartil 2024 | IF 2024 | APC obrigatório? | Aderência ao tema |
| --- | --- | --- | --- | --- | --- |
| **Engineering Failure Analysis** | Elsevier (subscription) | Q1 | 6,22 | Não — gratuito por trilha *subscription* | Falha mecânica de componentes — máxima aderência |
| **Mechanical Systems and Signal Processing** | Elsevier (subscription) | Q1 | — (SJR 2,64) | Não — gratuito por trilha *subscription* | Dinâmica de sistemas mecânicos, vibração, análise modal |
| **International Journal of Engine Research** | SAGE (subscription, IMechE) | Q2 | — (SJR 0,56) | Não — gratuito por trilha *subscription* | Pesquisa em motores SI; público específico do tema |
| **Proc. IMechE Part D — J. of Automobile Engineering** | SAGE (subscription, IMechE) | Q2 | 2,62 | Não — gratuito por trilha *subscription* | Engenharia automotiva aplicada |

Recomendação primária: **Engineering Failure Analysis** — é Q1, tem foco direto em análise de falha mecânica e aceita estudos com BowTie. Backup: **Mechanical Systems and Signal Processing** se o eixo for análise modal/vibração; ou **IJER** / **IMechE Part D** se o orientador preferir comunidade de motoristas/mecânica automotiva.

> **SAE Technical Paper** foi removido como sugestão: não é uma revista Q1/Q2 indexada; é série de relatórios técnicos.

---

## Título 3 — Combustão anormal de espectro completo

**Mapeamento BowTie das Modalidades de Combustão Anormal (Knock, Pré-Ignição e LSPI) em Cabeçote de Alta Compressão a Etanol**

### Por que este título
O Título 1 trata só do knock. Este aqui amplia o escopo para as **três modalidades de combustão anormal** que a dissertação encadeia em 2.8 — knock, pré-ignição e ignição de superfície (LSPI quando há GDI e alta carga). Cada modalidade tem ameaças e barreiras parcialmente diferentes; o BowTie comparativo evidencia onde uma mesma barreira protege contra mais de um modo, e onde há barreiras dedicadas. É um artigo mais maduro metodologicamente, com potencial de citação cruzada entre as três literaturas.

### Aproveitamento direto da dissertação
- Item 2.8 inteiro (combustão anormal)
- Item 2.9 (etanol e suas propriedades antidetonantes — base contra-LSPI)
- Item 2.4.5 (alta TC: ganhos de eficiência e riscos de knock)
- CFD (Cap. 3.5) para campos térmicos locais

### Diferencial do Título 3 vs Título 1
Em vez de **um** evento topo, são **três BowTies sobrepostos**, com tabela de cruzamento de barreiras. Útil para discussão crítica que valoriza o lado *Sistemas de Engenharia* do programa de mestrado (visão integrada).

### Revistas-alvo do Título 3 (Q1, gratuitas — eixo combustão anormal)

| Revista | Editora | Quartil 2024 | IF 2024 | APC obrigatório? | Aderência ao tema |
| --- | --- | --- | --- | --- | --- |
| **Combustion and Flame** | Elsevier (subscription) | Q1 | 7,13 | Não — gratuito por trilha *subscription* | Knock, pré-ignição, LSPI — referência da área |
| **Fuel** | Elsevier (subscription) | Q1 | 8,78 | Não — gratuito por trilha *subscription* | Combustão de etanol e influência do combustível |
| **Energy Conversion and Management** | Elsevier (subscription) | Q1 | 12,42 | Não — gratuito por trilha *subscription* | Eficiência sob restrição de combustão anormal |
| **Reliability Engineering & System Safety** | Elsevier (subscription) | Q1 | 12,98 | Não — gratuito por trilha *subscription* | BowTie comparativo entre modos de falha — eixo de risco |

Recomendação primária: **Combustion and Flame** se o ângulo for físico-químico; **Reliability Engineering & System Safety** se o ângulo for o BowTie comparativo dos três modos.

---

## Título 4 — Acoplamento BowTie + IoT + IA (puxando o PDF "Avaliação Analítica dos Riscos…")

**Framework Integrado BowTie–IoT–Inteligência Artificial para Monitoramento Preditivo de Detonação e Falha do Trem de Válvulas em Motor AP 1.8**

### Por que este título
Já existe no diretório o PDF **"Avaliação Analítica dos Riscos de Detonação e Falha do Trem de Válvulas no Motor AP 1.8 com Aplicação da Metodologia BowTie, IoT e Inteligência Artificial"**. Esse PDF é, provavelmente, um **rascunho** ou material de partida para um artigo. Este título consolida esse rascunho num artigo formal e o **ancora na dissertação** (que fornece o modelo físico subjacente, sem o qual o IoT/IA seria caixa-preta sem fundamentação).

### Aproveitamento direto
- PDF auxiliar inteiro (`Avaliação Analítica dos Riscos…`)
- Capítulo 2 da dissertação (modelos físicos que justificam quais variáveis o IoT precisa medir)
- Estrutura BowTie já esboçada no PDF auxiliar — apenas formalizar e quantificar barreiras

### Diferencial conceitual
Aqui o BowTie deixa de ser **estático** (matriz qualitativa) e passa a ser **dinâmico**: as barreiras são monitoradas em tempo real via sensores IoT (vibração, pressão de câmara, temperatura, sinal de íon, fônon), e a IA atualiza a probabilidade de ativação do evento topo. Esse acoplamento é a **contribuição metodológica** do artigo — bem alinhado com "Sistemas de Engenharia".

### Risco a vigiar
Garantir que o IoT/IA **não invente dados**: ou se trabalha com dados sintéticos da CFD (declarados como tal), ou com bancada experimental real. Se não houver bancada, posicionar como **proposta de framework** e validá-lo via simulação.

### Revistas-alvo do Título 4 (Q1, gratuitas — eixo IA/IoT/sistemas)

| Revista | Editora | Quartil 2024 | IF 2024 | APC obrigatório? | Aderência ao tema |
| --- | --- | --- | --- | --- | --- |
| **Engineering Applications of Artificial Intelligence** | Elsevier (subscription) | Q1 | 10,23 | Não — gratuito por trilha *subscription* | IA aplicada a engenharia — máxima aderência |
| **Mechanical Systems and Signal Processing** | Elsevier (subscription) | Q1 | — (SJR 2,64) | Não — gratuito por trilha *subscription* | Sinais de IoT (vibração, pressão, ion-current) e ML |
| **Reliability Engineering & System Safety** | Elsevier (subscription) | Q1 | 12,98 | Não — gratuito por trilha *subscription* | BowTie dinâmico, monitoramento preditivo |
| **Process Safety and Environmental Protection** | IChemE/Elsevier (subscription) | Q1 | 8,82 | Não — gratuito por trilha *subscription* | BowTie + IoT em segurança de processo |

Recomendação primária: **Engineering Applications of Artificial Intelligence** se o IoT/IA for o foco; **Reliability Engineering & System Safety** se o BowTie dinâmico for o foco.

> **IEEE Access** foi removido como sugestão: APC obrigatório de US\$ 2.160 (2026) — não atende ao critério de gratuidade. Há descontos para autores em países classificados como baixa renda pelo Banco Mundial, mas o Brasil **não** se enquadra nessa lista.

---

## Título 5 — Integração BowTie ao processo de otimização (mais metodológico)

**Otimização Multiobjetivo de Cabeçote de Alta Performance Sob Restrições de Risco: Integração da Metodologia BowTie ao Framework de Projeto Termo-Fluidodinâmico**

### Por que este título
Os títulos 1–4 usam BowTie sobre algo já projetado. Este título inverte: **o BowTie entra como restrição do problema de otimização**. A dissertação descreve, no Cap. 2.11, a otimização multiobjetivo do cabeçote (Pareto, metamodelagem); o gap conceitual é que a função-objetivo só fala em **eficiência/consumo/vazão** e as restrições são geométricas. Aqui as **barreiras quantitativas extraídas do BowTie viram restrições explícitas** do problema (ex.: margem antidetonante mínima, frequência natural da mola acima de uma harmônica crítica do came, temperatura máxima de parede da câmara).

### Aproveitamento direto da dissertação
- Cap. 2.11 inteiro (otimização computacional do cabeçote)
- Cap. 2.4, 2.6, 2.8 (formulação física que alimenta as restrições BowTie)
- Cap. 3.6 (procedimento de validação e indicadores)

### Contribuição central
Mostrar que **otimizar sem restrição de risco produz pontos de Pareto inviáveis** (ex.: TC máxima sem checar margem antidetonante, ou eficiência volumétrica máxima sem checar tempo de comutação do trem de válvulas). O BowTie é a ponte entre "ótimo termodinâmico" e "ótimo confiável".

### Por que é o título mais forte do ponto de vista de mestrado em Sistemas de Engenharia
Articula explicitamente os dois mundos do programa: **modelagem física + análise sistêmica de risco**. Um avaliador externo lê a contribuição metodológica de imediato. Os outros quatro títulos são bons artigos de aplicação; este aqui é um artigo **de método**.

### Revistas-alvo do Título 5 (Q1, gratuitas — eixo metodológico/otimização sob risco)

| Revista | Editora | Quartil 2024 | IF 2024 | APC obrigatório? | Aderência ao tema |
| --- | --- | --- | --- | --- | --- |
| **Reliability Engineering & System Safety** | Elsevier (subscription) | Q1 | 12,98 | Não — gratuito por trilha *subscription* | Otimização sob restrição de confiabilidade — máxima aderência |
| **Process Safety and Environmental Protection** | IChemE/Elsevier (subscription) | Q1 | 8,82 | Não — gratuito por trilha *subscription* | BowTie integrado a projeto de processo |
| **Energy Conversion and Management** | Elsevier (subscription) | Q1 | 12,42 | Não — gratuito por trilha *subscription* | Otimização termo-energética com restrição prática |
| **Engineering Applications of Artificial Intelligence** | Elsevier (subscription) | Q1 | 10,23 | Não — gratuito por trilha *subscription* | Se a otimização usar metamodelagem/ML |

Recomendação primária: **Reliability Engineering & System Safety** — é o periódico que melhor reconhece a contribuição metodológica de "otimização sob restrição de risco". É também onde estudos de BowTie quantitativo costumam ser publicados.

> Periódicos descartados deste título: *Structural and Multidisciplinary Optimization* (Springer, Q1, mas modelo híbrido com pressão de APC para autores sem acordo institucional — risco de não ser efetivamente gratuito); *IEEE Access* (APC US\$ 2.160).

---

## Tabela comparativa rápida

| # | Foco | Eixo dominante | Distância até artigo pronto | Risco principal |
|---|------|----------------|------------------------------|-----------------|
| 1 | Knock | Combustão | Curta — Cap. 2.8 + 2.9 quase prontos | Repetir conteúdo de literatura sem dado novo |
| 2 | Trem de válvulas | Mecânica | Curtíssima — PDFs de cálculo já existem | Ser visto como engenharia de cálculo, sem novidade científica |
| 3 | Combustão anormal completa | Combustão | Média — exige tabela cruzada de barreiras | Escopo grande para 8–12 páginas |
| 4 | BowTie + IoT + IA | Sistemas | Média — depende de dados (sintéticos ou reais) | Ser caixa-preta se não houver dataset real |
| 5 | BowTie como restrição de otimização | Metodologia | Maior — exige reformular a otimização da dissertação | Carga conceitual alta, mas é o mais original |

---

## Recomendação

Para um aluno de mestrado que precisa **um artigo publicável já no curto prazo** sem inventar dados: **Título 2** (trem de válvulas a 10.000 rpm) é o de menor risco — os cálculos já existem nos PDFs auxiliares e o BowTie estrutura o que está disperso.

Para um aluno que quer um artigo com **maior valor científico/metodológico** e está disposto a investir mais tempo: **Título 5** (BowTie como restrição da otimização) é o de maior diferencial.

Para extrair valor do que **já está esboçado no diretório**: **Título 4**, que consolida o PDF "Avaliação Analítica dos Riscos…" num formato de artigo formal ancorado na dissertação.

Os Títulos 1 e 3 são alternativas sólidas se o orientador preferir foco em combustão.

---

## Tabela mestre de revistas — Q1/Q2 e gratuitas (sem APC obrigatório)

Lista consolidada das nove revistas usadas neste documento, todas com **possibilidade de publicação gratuita pela trilha subscription** e classificação **Q1 ou Q2 no Scimago (SJR)** em 2024. As revistas são todas de editoras com longa tradição em engenharia (Elsevier, SAGE, IChemE) — o que dá segurança quanto à validade da indexação para CAPES e DOI persistente.

| # | Revista | Editora | Quartil 2024 | IF 2024 | SJR 2024 | APC OA opcional* | Onde se aplica neste documento |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **Fuel** | Elsevier | Q1 | 8,78 | 1,61 | US\$ 4.080 | Títulos 1, 3 |
| 2 | **Combustion and Flame** | Elsevier | Q1 | 7,13 | 2,02 | variável | Títulos 1, 3 |
| 3 | **Applied Thermal Engineering** | Elsevier | Q1 | 7,86 | 1,58 | US\$ 3.480 | Título 1 |
| 4 | **Energy Conversion and Management** | Elsevier | Q1 | 12,42 | 2,66 | US\$ 4.370 | Títulos 3, 5 |
| 5 | **Engineering Failure Analysis** | Elsevier | Q1 | 6,22 | 1,16 | US\$ 3.690 | Título 2 |
| 6 | **Mechanical Systems and Signal Processing** | Elsevier | Q1 | — | 2,64 | US\$ 4.760 | Títulos 2, 4 |
| 7 | **Engineering Applications of Artificial Intelligence** | Elsevier | Q1 | 10,23 | 1,65 | US\$ 3.040 | Títulos 4, 5 |
| 8 | **Reliability Engineering & System Safety** | Elsevier | Q1 | 12,98 | 2,65 | US\$ 4.590 | Títulos 3, 4, 5 |
| 9 | **Process Safety and Environmental Protection** | IChemE/Elsevier | Q1 | 8,82 | 1,47 | US\$ 3.450 | Títulos 4, 5 |
| 10 | **International Journal of Engine Research** | SAGE | Q2 | — | 0,56 | sem cobrança obrigatória | Título 2 |
| 11 | **Proc. IMechE Part D — J. of Automobile Engineering** | SAGE | Q2 | 2,62 | 0,50 | sem cobrança obrigatória | Título 2 |

*Coluna "APC OA opcional": valor cobrado **apenas se** o autor optar voluntariamente pela trilha *gold open access*. Submetendo pela trilha *subscription* (modelo tradicional), **não há cobrança** — o leitor/instituição paga assinatura. Todos os 11 periódicos da lista permitem essa escolha.

### Critérios usados na seleção

1. **Quartil:** Q1 ou Q2 no Scimago (SJR) na avaliação de 2024 (publicada em 2025)
2. **Gratuidade para o autor:** trilha *subscription* explicitamente disponível, sem cobrança
3. **Indexação:** Scopus, Web of Science Core Collection (qualifica para Qualis CAPES sob qualquer dos critérios bibliométricos do novo ciclo 2025–2028)
4. **Aderência temática:** o escopo declarado da revista cobre BowTie, motores SI, combustão de etanol, falha mecânica, IA/IoT em engenharia, otimização sob restrição, ou confiabilidade
5. **DOI persistente e revisão por pares:** condição mínima para reconhecimento curricular no programa de mestrado

### Critérios usados para descartar

- **APC obrigatório > US\$ 0** mesmo na trilha tradicional (eliminou: IEEE Access, todas as revistas MDPI, Frontiers)
- **Quartil Q3 ou Q4** (não atende ao requisito explicitado pelo usuário)
- **Periódicos puramente locais ou sem indexação Scopus/WoS**
- **Séries de relatórios técnicos** (eliminou: SAE Technical Paper)

### Aviso sobre o Qualis CAPES

A partir do ciclo avaliativo **2025–2028**, a CAPES descontinuou o sistema Qualis Periódicos como classificação fixa por revista. A nova avaliação migra para indicadores bibliométricos diretos do artigo (citações, SJR, JCR Quartiles, altmetria) combinados com critérios qualitativos definidos por cada área. Todas as 11 revistas desta tabela atendem aos indicadores que substituem o Qualis na nova avaliação — Q1/Q2 do Scimago e indexação dupla Scopus + WoS.

---

*Documento gerado a partir da leitura das páginas 1–22 da dissertação `dissertacao.pdf` e dos três PDFs auxiliares presentes no diretório do projeto. Métricas das revistas (IF, SJR, quartil, APC) coletadas via Scimago, Resurchify, Elsevier ScienceDirect, IEEE Author Center e SAGE Publishing — referências completas no chat de origem. Nenhum dado, referência ou resultado foi inventado.*
