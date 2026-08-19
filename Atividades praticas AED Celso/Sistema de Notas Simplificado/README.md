# Atividade Prática 1 — Sistema de Notas Simplificado

## 📚 Disciplina

**Algoritmos e Estrutura de Dados**
**Faculdade:** Celso Lisboa
**Linguagem:** Python
**Fase:** 1
**Atividade:** Processamento de Dados com Loops — Parte 3

## 📌 Sobre a atividade

Esta atividade prática tem como objetivo aplicar **estruturas de repetição** para processar um conjunto de dados, realizar cálculos e desenvolver uma solução capaz de trabalhar com múltiplas informações.

Nesta parte da atividade, foi desenvolvido um **Sistema de Notas Simplificado**, responsável por receber as notas de cinco alunos, calcular suas médias individuais, classificá-los como aprovados ou reprovados e apresentar um relatório final da turma.

O enunciado da faculdade determina que sejam calculadas as médias de três notas para cada um dos cinco alunos, utilizando loops aninhados para percorrer os alunos e suas respectivas notas.

O enunciado completo da atividade está disponível neste repositório em formato PDF.

---

# 👨‍🎓 Processamento das notas dos alunos

O programa permite cadastrar **cinco alunos por execução**.

Para cada aluno, o sistema solicita:

* Nome do aluno;
* Três notas;
* Validação das notas;
* Cálculo da média;
* Classificação como aprovado ou reprovado.

A estrutura principal do programa utiliza um loop para percorrer os cinco alunos e um segundo loop, aninhado, para solicitar as três notas de cada aluno.

Essa utilização de loops aninhados atende diretamente ao requisito apresentado no enunciado.

---

# 🔄 Loops utilizados

## Loop dos alunos

O primeiro `for` é responsável por controlar a quantidade de alunos processados:

```python
for aluno in range(5):
```

Dessa forma, o programa executa o processamento exatamente cinco vezes.

## Loop das notas

Dentro do loop dos alunos existe um segundo `for`, responsável por solicitar as três notas:

```python
for nota in range(3):
```

Esse é um exemplo de **loop aninhado**, no qual um loop é executado dentro de outro.

A utilização dessa estrutura permite que o programa processe automaticamente três notas para cada um dos cinco alunos.

---

# ✅ Validação das notas

Para garantir que sejam inseridos somente valores válidos, foi utilizado um loop `while` dentro do processamento das notas.

O programa verifica se a nota está entre **0 e 10**.

```python
if nota > 10 or nota < 0:
    print("Nota inválida! Digite uma nota de 0 a 10.")
    continue
```

Caso seja informada uma nota fora desse intervalo, o sistema apresenta uma mensagem de erro e solicita uma nova entrada.

Essa validação corresponde ao requisito da atividade de solicitar e validar as três notas de cada aluno considerando valores entre 0 e 10.

---

# 🧮 Cálculo da média

Após receber as três notas válidas, o programa soma os valores e calcula a média do aluno:

```python
media = soma_nota / 3
```

A média é apresentada com duas casas decimais:

```python
print(f"A média do aluno {aluno} é igual a {media:.2f}")
```

---

# 📊 Classificação dos alunos

Após calcular a média, o programa verifica a situação de cada aluno.

A regra utilizada é:

```text
Média ≥ 7 → Aprovado
Média < 7 → Reprovado
```

Essa regra segue exatamente o critério definido no enunciado da atividade.

Os alunos são separados em duas listas:

```python
alunos_aprovados = []
alunos_reprovados = []
```

Quando um aluno é aprovado, seus dados são adicionados à lista `alunos_aprovados`.

Quando é reprovado, seus dados são adicionados à lista `alunos_reprovados`.

---

# 📈 Média geral da turma

Além das médias individuais, o programa também calcula a média geral da turma.

Para isso, as médias dos cinco alunos são acumuladas na variável:

```python
soma_da_media_turma = 0
```

Ao final do processamento, a média da turma é calculada:

```python
media_turma = soma_da_media_turma / 5
```

O resultado é apresentado no relatório final.

A apresentação da média da turma e da quantidade de alunos aprovados e reprovados faz parte dos resultados solicitados pela atividade.

---

# 📋 Relatório final

Após processar todos os alunos, o programa apresenta um relatório contendo:

* Lista de alunos aprovados;
* Lista de alunos reprovados;
* Média da turma.

Exemplo da estrutura apresentada pelo programa:

```text
📊 Relatório final da turma!

Total de alunos aprovados [...]
Total de alunos reprovados [...]

Média da turma: [...]
```

Dessa forma, o usuário consegue visualizar o resultado geral do processamento dos dados.

---

# 🧠 Conceitos praticados

Durante o desenvolvimento desta atividade foram trabalhados os seguintes conceitos:

* Estruturas de repetição;
* `for`;
* `while`;
* Loops aninhados;
* Listas;
* Entrada de dados;
* Validação de dados;
* Operadores condicionais;
* Estruturas `if` e `else`;
* Cálculo de médias;
* Acumuladores;
* Organização de dados;
* Formatação de saída;
* Processamento de múltiplos registros.

A atividade também avalia o uso correto de estruturas de repetição, a precisão dos cálculos, a utilização de loops aninhados e a eficiência das soluções propostas.

---

# ▶️ Como executar

É necessário ter o **Python 3** instalado.

Execute o arquivo pelo terminal:

```bash
python mediadeumaturma.py
```

Ou, em sistemas que utilizam o comando `python3`:

```bash
python3 mediadeumaturma.py
```

Após iniciar o programa, serão solicitados os nomes dos cinco alunos e suas respectivas três notas.

Ao final, o sistema exibirá o relatório geral da turma.

---

# 📁 Arquivos do exercício

```text
exercicio-01/
│
├── README.md
├── mediadeumaturma.py
└── Atividade pratica fase 1.pdf
```

O arquivo `Atividade pratica fase 1.pdf` contém a atividade proposta pela faculdade, enquanto o arquivo Python contém a solução desenvolvida para a **Parte 3 — Sistema de Notas Simplificado**.

---

# 🎯 Objetivo

O objetivo desta atividade foi desenvolver uma solução em Python capaz de processar as notas de diferentes alunos utilizando **loops e loops aninhados**, realizar cálculos e validações, classificar os alunos de acordo com suas médias e apresentar um relatório final com os resultados da turma.
