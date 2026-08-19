# Atividade Prática 3 — Do Dado Bruto ao KPI Temporal

## 📚 Disciplina

**Algoritmos e Estrutura de Dados**
**Faculdade:** Celso Lisboa
**Linguagem:** Python
**Fase:** 3

## 📌 Sobre a atividade

Esta atividade prática tem como objetivo trabalhar o processamento e a análise de dados de vendas a partir de um arquivo **CSV**, aplicando conceitos de leitura e tratamento de dados, cálculo de **KPIs**, análise temporal, utilização de **pilha** e persistência de informações em formato **JSON**.

A proposta da atividade consiste em transformar dados brutos de vendas em informações organizadas, permitindo analisar o faturamento e o lucro mensal, além de calcular a variação do faturamento entre os dois meses mais recentes.

O enunciado completo da atividade está disponível neste repositório em formato PDF.

---

# 📊 Parte 1 — Leitura e pré-processamento dos dados

O programa realiza a leitura do arquivo `vendas_online.csv` utilizando o módulo `csv` da biblioteca padrão do Python.

Para cada registro de venda, os dados são tratados antes de serem armazenados:

* `ValorVenda` é convertido para `float`;
* `CustoProduto` é convertido para `float`;
* `Data` é convertida para um objeto `datetime.date`.

Após o processamento, cada venda é armazenada como um dicionário dentro de uma lista.

Essa etapa atende à proposta do enunciado de realizar a leitura do arquivo CSV e converter os dados para os tipos apropriados.

### 🔧 Função utilizada

```python
def carregar_dados_vendas(vendas_online: str) -> list:
```

A função recebe o nome do arquivo CSV, realiza a leitura dos registros e retorna uma lista contendo os dados das vendas processadas.

---

# 💰 Parte 2 — Cálculo dos KPIs mensais

Após o carregamento dos dados, o programa utiliza a função:

```python
def calcular_faturamento_lucro_mensal(dados_vendas: list) -> dict:
```

Essa função percorre os registros de vendas e agrupa os dados de acordo com o mês no formato:

```text
AAAA-MM
```

Para cada mês são calculados dois indicadores:

### Faturamento

Representa a soma dos valores de venda realizados durante o mês.

### Lucro

É calculado pela diferença entre o valor de venda e o custo do produto:

```text
Lucro = ValorVenda - CustoProduto
```

O resultado é armazenado em um dicionário contendo o faturamento e o lucro de cada mês.

O enunciado determina justamente que os dados sejam agrupados por mês e que sejam calculados o faturamento e o lucro total de cada período.

---

# ⏱️ Análise de complexidade — Big O

A função `calcular_faturamento_lucro_mensal()` possui complexidade de tempo **O(n)**.

Isso ocorre porque a função percorre a lista de vendas uma única vez. Dessa forma, à medida que a quantidade de registros aumenta, o número de operações realizadas cresce de maneira proporcional à quantidade de vendas.

No próprio código foi incluído um comentário explicando essa complexidade, conforme solicitado no enunciado da atividade.

---

# 📚 Parte 3 — Análise temporal utilizando uma pilha

Para realizar a análise temporal, foi utilizada uma **lista Python como estrutura de pilha**.

A pilha utilizada foi:

```python
historico_faturamento_mensal_pilha = []
```

Após o cálculo dos indicadores mensais, cada mês e seu respectivo faturamento são armazenados como uma tupla:

```python
(mes, faturamento)
```

O objetivo é manter um histórico dos faturamentos mensais e permitir a consulta dos dois últimos registros.

Essa abordagem segue a proposta da atividade, que solicita a utilização de uma pilha para armazenar o histórico de faturamento mensal.

---

# 📈 Variação do faturamento

Para calcular a variação percentual entre os dois meses mais recentes, foi criada a função:

```python
def calcular_variacao_ultimo_mes(
    pilha_historico: list
) -> float | None:
```

A função verifica inicialmente se existem pelo menos dois registros na pilha.

Em seguida, consulta os dois últimos valores armazenados, sem removê-los permanentemente, e calcula a variação percentual utilizando a seguinte fórmula:

```text
Variação (%) =
((Faturamento atual - Faturamento anterior)
 / Faturamento anterior) × 100
```

Essa implementação atende à orientação do enunciado de consultar os dois últimos registros da pilha sem removê-los durante a análise.

---

# 💾 Persistência dos resultados

Após o processamento dos dados, o programa salva o resumo das métricas em um arquivo **JSON**.

Para isso, foi criada a função:

```python
def salvar_sumario_metricas(
    sumario: dict,
    nome_arquivo_json: str
) -> None:
```

A função utiliza o módulo `json` para transformar o dicionário de resultados em um arquivo JSON organizado.

O arquivo gerado pelo programa é:

```text
resumo_vendas.json
```

Essa etapa atende à segunda parte da atividade, que solicita a criação de uma função para salvar os resultados do cálculo de faturamento e lucro em formato JSON.

---

# 📊 Resultados obtidos

Com os dados utilizados no exercício, foram obtidos os seguintes resultados:

| Mês     | Faturamento |     Lucro |
| ------- | ----------: | --------: |
| 2026-04 | R$ 2.030,00 | R$ 835,00 |
| 2026-05 | R$ 2.060,00 | R$ 935,00 |
| 2026-06 | R$ 2.070,00 | R$ 840,00 |

A variação do faturamento entre **maio e junho** foi de aproximadamente **0,49%**, indicando um pequeno aumento no faturamento do mês mais recente.

---

# 🧠 Conceitos praticados

Durante o desenvolvimento da atividade foram trabalhados os seguintes conceitos:

* Leitura de arquivos CSV;
* Conversão e tratamento de dados;
* Listas;
* Dicionários;
* Tuplas;
* Funções;
* KPIs de faturamento e lucro;
* Agrupamento de dados por período;
* Análise temporal;
* Estrutura de dados do tipo pilha;
* Cálculo de variação percentual;
* Análise de complexidade Big O;
* Persistência de dados;
* Arquivos JSON;
* Docstrings e organização do código.

## Esses conceitos correspondem aos objetivos e critérios de avaliação apresentados no enunciado da atividade.

# ▶️ Como executar

Para executar o projeto, é necessário ter o **Python 3** instalado.

Os arquivos necessários são:

```text
vendas_onine.py
vendas_online.csv
```

Execute o programa pelo terminal:

```bash
python vendas_onine.py
```

Ou, em sistemas que utilizam o comando `python3`:

```bash
python3 vendas_onine.py
```

Após a execução, o programa:

1. Lê os dados do arquivo CSV;
2. Exibe os registros processados;
3. Calcula o faturamento e o lucro mensal;
4. Exibe os KPIs mensais;
5. Cria o histórico de faturamento utilizando uma pilha;
6. Calcula a variação entre os dois últimos meses;
7. Salva o resumo das métricas no arquivo `resumo_vendas.json`.

---

# 📁 Arquivos do exercício

```text
exercicio-03/
│
├── README.md
├── vendas_onine.py
├── vendas_online.csv
├── resumo_vendas.json
└── Atividade prática 3.pdf
```

O arquivo `Atividade prática 3.pdf` contém a atividade proposta pela faculdade, enquanto os demais arquivos correspondem à implementação e aos resultados desenvolvidos neste exercício.

---

# 🎯 Objetivo

O objetivo desta atividade foi aplicar conceitos de **Algoritmos e Estrutura de Dados** ao processamento de dados de vendas, demonstrando como informações inicialmente armazenadas em um arquivo CSV podem ser transformadas em indicadores mensais, analisadas temporalmente por meio de uma pilha e posteriormente persistidas em um arquivo JSON.
