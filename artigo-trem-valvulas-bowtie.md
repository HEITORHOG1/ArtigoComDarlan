# Dossiê do Artigo — Trem de Válvulas a 10.000 rpm + BowTie

**Status:** proposta para análise/decisão com orientador
**Origem:** recorte temático da dissertação de Darlan Costa Porto (UCP, Mestrado em Sistemas de Engenharia, 2026)
**Documento-pai:** [titulos-artigo-bowtie.md](titulos-artigo-bowtie.md) — este dossiê detalha o Título 2

---

## 1. Título

### Versão A (recomendada — mais conservadora)

> **Análise BowTie do Trem de Válvulas de Motor AP 1.8 Operando a 10.000 rpm com Cabeçote de Alta Performance**

### Versão B (alternativa, mais formal)

> **Avaliação Integrada de Risco do Trem de Válvulas em Cabeçote de Alta Performance Concebido para Motor AP 1.8 a 10.000 rpm pela Metodologia BowTie**

### Por que **NÃO** usar a versão original com "Otimizado"

A palavra *"otimizado"* implica resultado de uma otimização já executada — algo que a dissertação ainda **não** produziu (o Cap. 2.11 da dissertação é descrição do método de otimização, não do resultado). Banca pode exigir prova do otimizado. **"Concebido"** ou **"operando com cabeçote de alta performance"** são afirmações que a dissertação respalda integralmente.

---

## 2. Posicionamento estratégico

### Por que este título é o de menor risco entre os 5 propostos

| Dimensão | Avaliação |
| --- | --- |
| **Material disponível** | Alto — PDFs `CALCULO DA VALVULA DE ADMISSÃO PARA 10.000RPM.pdf` e `CALCULO DAS MOLAS PARA 10.000RPM.pdf` já contêm a base analítica |
| **Aderência à dissertação** | Direta — itens 2.3.7, 3.2.7 da dissertação tratam exatamente disso |
| **Aderência ao venue (Engineering Failure Analysis)** | Alta — BowTie de modo de falha mecânico é exatamente o que a revista publica |
| **Esforço incremental** | Baixo — o artigo estrutura material existente, não exige bancada nova |
| **Defensibilidade pela banca** | Alta — fenômeno físico claro, calculável, auditável |
| **Cronograma realista** | 2–4 meses (texto + revisão) |

### Por que este artigo é cientificamente válido (não é só "engenharia de cálculo")

A contribuição é **metodológica + aplicada simultaneamente**:

1. **Aplicada:** mapeia, com BowTie, todos os caminhos pelos quais o trem de válvulas pode falhar a 10.000 rpm em motor AP 1.8 — informação útil para fabricantes de cabeçotes de alta performance no Brasil
2. **Metodológica:** acopla BowTie qualitativo a uma camada quantitativa baseada em cálculos analíticos (frequências naturais, margens de coil bind, fadiga). Esse acoplamento é a inovação que diferencia o artigo de um estudo puramente narrativo

---

## 3. Aproveitamento direto da dissertação e dos PDFs auxiliares

### Da dissertação (`dissertacao.pdf`, 232 fls., 7 capítulos)

- **Item 2.3.7** — Requisitos mecânicos do trem de válvulas para 10.000 rpm
- **Item 3.2.6** — Premissas operacionais e regime de rotação
- **Item 3.2.7** — Premissas mecânicas e construtivas do trem de válvulas
- **Item 3.2.2 e 3.2.3** — Premissas geométricas e de admissão (fornecem contexto da câmara/dutos para o trem)
- **Capítulo 1.6** — Justificativa (relevância tecnológica do AP 1.8 no contexto brasileiro)

### Dos PDFs auxiliares (já existentes no diretório)

- **`CALCULO DA VALVULA DE ADMISSÃO PARA 10.000RPM.pdf`** — dimensionamento da válvula, área efetiva, levantamento, materiais
- **`CALCULO DAS MOLAS PARA 10.000RPM.pdf`** — rigidez, frequências naturais, margem de coil bind, fadiga
- **`Avaliação Analítica dos Riscos de Detonação e Falha do Trem de Válvulas no Motor AP 1.8 …BowTie, IoT e IA.pdf`** — esboço inicial do BowTie do trem de válvulas (já contém o evento topo e algumas barreiras — pode ser usado como ponto de partida da estrutura)

### O que **não** existe ainda (lacunas a fechar)

- Análise modal experimental ou por elementos finitos (pode ser substituída por análise analítica de frequência natural × harmônicas do came — usar dados dos PDFs)
- Dados de fadiga reais (suprir com curvas S–N de catálogo de aços de mola — citar referência, não inventar)
- Validação experimental em bancada (declarar limitação aberta na conclusão)

---

## 4. Estrutura BowTie proposta

### Nível qualitativo

```
                    [Ameaças/causas]                                    [Consequências]
                                          ╲                       ╱
   1. Rigidez insuficiente da mola         ╲                     ╱   1. Colisão válvula/pistão
   2. Massa móvel excessiva                 ╲                   ╱    2. Falha catastrófica do cabeçote
   3. Perfil agressivo do came               ╲                 ╱     3. Queda imediata de compressão
   4. Aquecimento da mola (perda K)           ╲   EVENTO TOPO ╱      4. Contaminação do óleo por debris
   5. Folga térmica fora de tolerância         ╲             ╱       5. Parada não programada do motor
   6. Ressonância na rotação operacional        ╲           ╱
                                                  ╲   ⊗   ╱
                                                   ╲     ╱
                                            Perda de seguimento
                                            válvula↔came
                                            (valve float / bounce /
                                             aproximação ao coil bind)
                                                   ╱     ╲
                                                  ╱       ╲
        [Barreiras preventivas]                  ╱         ╲       [Barreiras mitigadoras]
                                                ╱           ╲
   1. Dimensionamento dinâmico                 ╱             ╲   1. Limitador eletrônico de rotação
      (f_natural_mola vs harmônica do came)   ╱               ╲  2. Sensor de posição do came (knock no came)
   2. Molas duplas (redundância)              ╱                ╲ 3. Janela operacional definida em projeto
   3. Tuchos de baixa massa                                      4. Corte de torque / corte de injeção
   4. Materiais com alta resistência à fadiga                    5. Manutenção preditiva por sinais de vibração
   5. Análise modal e validação em dinamômetro
```

### Camada quantitativa (acoplamento ao cálculo analítico)

| Barreira preventiva | Indicador quantitativo | Critério de sucesso |
| --- | --- | --- |
| Frequência natural da mola | `f_n = (1/2π)·√(k_eff/m_eff)` | `f_n / f_came_max ≥ 4` (regra de projeto Heisler/Mendes para motores SI de alta rotação) |
| Margem de coil bind | `δ_disponível = L_comprimida_total − L_max_came` | `δ ≥ 0,15·δ_total` (margem mínima de 15%) |
| Fadiga da mola | `σ_torção_máx` vs limite S–N do material | `σ_máx / σ_lim ≤ 0,5` (FoS=2) |
| Massa móvel × levantamento | inércia translacional `m·a_pico` | comparação com pré-carga útil disponível na mola |
| Folga térmica | variação dimensional com `ΔT` | folga residual quente ≥ 0 em qualquer ponto do mapa |

> **Nota metodológica:** declarar explicitamente que os critérios numéricos (FoS=2, margem 15%, razão ≥ 4) são **valores de projeto adotados a partir da literatura de motores SI**. Citar referências reais (Heywood, Stone, Taylor) em vez de inventá-las.

---

## 5. Estrutura preliminar do artigo (8–12 páginas, formato Engineering Failure Analysis)

```
1. Introduction                                 ~1,0 pg
   1.1 Motor AP 1.8 no contexto brasileiro
   1.2 Por que 10.000 rpm muda o regime do trem de válvulas
   1.3 Limitações do FMEA tradicional para esse problema
   1.4 Proposta: BowTie quantitativo
   1.5 Contribuições do artigo

2. Background                                   ~1,5 pg
   2.1 Modos de falha do trem de válvulas em alta rotação
       (valve float, bounce, coil bind, fadiga)
   2.2 Metodologia BowTie: revisão concisa
   2.3 Trabalhos correlatos (revisão narrativa, ~10 refs)

3. Methodology                                  ~2,0 pg
   3.1 Sistema em estudo: cabeçote de alta performance AP 1.8
   3.2 Premissas mecânicas e operacionais (10.000 rpm)
   3.3 Construção do BowTie qualitativo
   3.4 Camada quantitativa: indicadores e critérios
   3.5 Procedimento de cruzamento qualitativo↔quantitativo

4. Results                                      ~3,0 pg
   4.1 BowTie do evento topo "perda de seguimento válvula↔came"
   4.2 Quantificação das barreiras preventivas
        Tab. 1 — Frequências naturais vs harmônicas do came
        Tab. 2 — Margens de coil bind por configuração
        Tab. 3 — Fator de segurança à fadiga
        Fig. 1 — Diagrama BowTie completo
        Fig. 2 — Tornado plot de sensibilidade
   4.3 Identificação da barreira crítica

5. Discussion                                   ~1,5 pg
   5.1 Implicações para o projeto do cabeçote
   5.2 Comparação com critério tradicional FMEA/RPN
   5.3 Limitações do estudo (sem bancada)

6. Conclusion                                   ~0,5 pg

References                                      ~0,5 pg (15-25 refs)
```

### Figuras planejadas (mínimo 4)

- **Fig. 1** — Diagrama BowTie integrado (o desenho completo)
- **Fig. 2** — Curva de levantamento da válvula × ângulo de manivela (do PDF auxiliar)
- **Fig. 3** — Frequências naturais da mola × harmônicas do came em função da rotação
- **Fig. 4** — Tornado plot de sensibilidade das barreiras
- *(opcional)* **Fig. 5** — Mapa de operação seguro × inseguro no espaço (rotação, levantamento)

### Tabelas planejadas (3)

- **Tab. 1** — Premissas geométricas e operacionais do AP 1.8 (do item 3.2 da dissertação)
- **Tab. 2** — Indicadores quantitativos das barreiras preventivas (com critério e valor calculado)
- **Tab. 3** — Mapeamento ameaça → barreira → consequência → barreira mitigadora

---

## 6. Revistas-alvo (Q1/Q2, gratuitas — sem APC obrigatório)

### Recomendação primária

| Revista | **Engineering Failure Analysis** |
| --- | --- |
| Editora | Elsevier (modelo subscription) |
| Quartil 2024 | **Q1** |
| Impact Factor 2024 | 6,22 |
| SJR 2024 | 1,16 |
| h-index | 113 |
| APC obrigatório | **Não** — gratuito pela trilha *subscription*. APC só se autor optar por gold OA (US\$ 3.690 — opcional) |
| Indexação | Scopus, Web of Science Core Collection |
| Aderência ao tema | **Máxima** — o periódico publica regularmente análises BowTie de modos de falha mecânicos |
| URL | https://www.sciencedirect.com/journal/engineering-failure-analysis |

**Por que ela é a melhor opção:**

1. Casa entre metodologia (BowTie) e venue
2. Aceita estudos de caso aplicados sem exigir bancada experimental
3. Comunidade leitora é exatamente o público-alvo do artigo (engenheiros automotivos e de confiabilidade)
4. Q1 sólido — o programa de mestrado reconhece sem ressalvas

### Backups por ângulo

| Revista | Quartil | IF/SJR | Quando preferir | APC obrigatório |
| --- | --- | --- | --- | --- |
| **Mechanical Systems and Signal Processing** | Q1 | SJR 2,64 | Se o ângulo dominante for **análise modal e processamento de sinal vibratório** | Não |
| **International Journal of Engine Research** | Q2 | SJR 0,56 | Se o orientador preferir a **comunidade específica de motores SI** (IMechE) | Não |
| **Proc. IMechE Part D — J. of Automobile Engineering** | Q2 | IF 2,62 | Se o ângulo for **engenharia automotiva aplicada genérica** | Não |

### Revistas explicitamente descartadas

- **IEEE Access** — APC US\$ 2.160 obrigatório (não atende ao critério "gratuito"). Brasil não está na lista de waiver
- **MDPI (Applied Sciences, Energies, etc.)** — APC obrigatório em todos os títulos
- **SAE Technical Papers** — não é revista indexada Q1/Q2; é série de relatórios técnicos
- **Frontiers** — APC obrigatório

---

## 7. Cronograma estimado (2–4 meses)

| Etapa | Duração | Saída |
| --- | --- | --- |
| **Etapa 1** — Levantamento bibliográfico (15–25 refs) | 2 sem | Lista de referências validadas com DOI |
| **Etapa 2** — Sistematização do BowTie qualitativo | 1 sem | Diagrama completo + tabela de mapeamento |
| **Etapa 3** — Cálculos quantitativos das barreiras (a partir dos PDFs) | 2 sem | Tabelas 2 e 3 + Figs. 3 e 4 preenchidas |
| **Etapa 4** — Redação primeira versão | 3 sem | Manuscrito v1 (8–12 pg) |
| **Etapa 5** — Revisão com orientador | 1–2 sem | Manuscrito v2 |
| **Etapa 6** — Submissão ao Engineering Failure Analysis | — | Sistema EVISE/EM |
| **Etapa 7** — Revisão de pares (estimativa Elsevier) | 8–16 sem | Major/minor revision |
| **Etapa 8** — Resposta aos revisores e re-submissão | 2–4 sem | Manuscrito final |

**Tempo total até aceite estimado:** 6–10 meses a partir do início do trabalho.

---

## 8. Pontos a validar com o orientador (Prof. José Cristiano Pereira) — **antes** de começar

1. **Política do programa sobre publicação pré-defesa:** o programa permite publicar parte da dissertação como artigo antes da defesa? Caso sim, há requisito de menção ao programa/orientador em "Acknowledgments"?
2. **Co-autoria:** ordem dos autores e inclusão do orientador como co-autor (padrão em mestrado é Darlan + Pereira)
3. **Posicionamento do artigo na narrativa da dissertação:** este artigo é **anterior** à defesa (capítulo da dissertação cita o artigo já submetido) ou **posterior** (defesa primeiro, artigo depois)?
4. **Alinhamento da Versão A vs B do título:** qual versão soa melhor para o orientador?
5. **Margem antidetonante e quench:** o artigo deve mencionar essas características do cabeçote (que estão na dissertação) ou se manter estritamente no trem de válvulas? Recomendação: menção breve no item 3.1, sem entrar em mérito
6. **Disponibilidade dos cálculos dos PDFs auxiliares para reprodução no artigo:** os números podem ser publicados? Há alguma proteção de IP ou segredo industrial?

---

## 9. Riscos identificados e mitigações

| Risco | Probabilidade | Mitigação |
| --- | --- | --- |
| Revisor cobrar dado experimental | Média | Declarar explicitamente como "estudo analítico-de-risco"; citar literatura experimental para validar premissas (Heywood, Stone) |
| Revisor cobrar comparação com FMEA/RPN tradicional | Alta | **Incluir** essa comparação no item 5.2 — vira ponto forte, não fraqueza |
| Banca questionar palavra "Otimizado" no título | Média (alta se mantida) | Usar Versão A ou B — eliminar "Otimizado" |
| BowTie ser visto como qualitativo demais | Média | Camada quantitativa (item 4 deste dossiê) é a defesa principal |
| Sobreposição com artigo de detonação (knock) caso ele venha depois | Baixa | Manter os dois artigos com escopos disjuntos: este só fala de mecânica do trem de válvulas |
| Artigo recortar a dissertação de forma a "esvaziá-la" | Baixa | O recorte é uma fatia de Cap. 2.3 + 3.2; a dissertação inteira tem 7 capítulos, dos quais este é < 10% |

---

## 10. Checklist de submissão (Engineering Failure Analysis)

- [ ] Manuscrito em inglês (idioma da revista)
- [ ] 8–12 páginas, fonte Elsevier (single-column LaTeX `elsarticle.cls` ou Word template)
- [ ] Abstract ≤ 250 palavras, com keywords (5–8)
- [ ] Highlights (3–5 bullets curtos) — exigido pela revista
- [ ] Graphical Abstract (figura única do BowTie) — recomendado
- [ ] Declaration of competing interests
- [ ] CRediT author statement (papel de cada autor)
- [ ] Data availability statement (apontar Zenodo ou repositório institucional UCP, se aplicável)
- [ ] Cover letter explicando o ângulo de novidade
- [ ] Carta de aprovação ética (não se aplica — estudo computacional)

---

## 11. Decisões abertas (precisam de input do Darlan e/ou orientador)

1. ☐ Versão A ou B do título?
2. ☐ Submeter ao **Engineering Failure Analysis** (recomendação) ou a um dos backups?
3. ☐ Cronograma — começar agora ou aguardar marco da dissertação?
4. ☐ O PDF auxiliar `Avaliação Analítica dos Riscos de Detonação e Falha do Trem de Válvulas…BowTie, IoT, IA.pdf` é incorporado a este artigo, ou é base de um segundo artigo (Título 4)? **Recomendação:** manter este artigo só com o trem de válvulas e a parte BowTie+IoT+IA vira artigo separado posterior, para não inflar escopo
5. ☐ Inclusão de quais referências âncora? Sugestão de partida: Heywood (Internal Combustion Engine Fundamentals), Stone (Introduction to ICE), Taylor (The IC Engine in Theory and Practice), de la Cruz et al. para BowTie em mecânica, periódico Engineering Failure Analysis 2020–2025 (≥ 5 artigos recentes)

---

*Dossiê construído a partir das páginas 1–22 da dissertação `dissertacao.pdf` e dos PDFs auxiliares. Métricas de revistas (IF, SJR, quartil, APC) verificadas via Scimago, Resurchify e Elsevier ScienceDirect (consulta de abril/2026). Nenhum dado, referência ou resultado foi inventado. Todas as afirmações sobre o conteúdo da dissertação remetem a seções identificáveis no sumário.*
