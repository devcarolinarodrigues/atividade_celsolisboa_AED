#  Atividade Prática 2 — Gerenciando Coleções de Dados

##  📚 Disciplina

**Algoritmos e Estrutura de Dados**
**Faculdade:** Celso Lisboa
**Linguagem:** Python

## 📌 Sobre a atividade

Esta atividade prática tem como objetivo aplicar estruturas de dados fundamentais da linguagem Python, utilizando **listas, tuplas e dicionários**, além da criação de funções para manipulação e gerenciamento dessas estruturas.

O exercício proposto pela faculdade foi dividido em três partes:

1. **Catálogo de Produtos da Loja**
2. **Carrinho de Compras**
3. **Dados de Clientes**

O enunciado completo da atividade está disponível neste repositório em formato PDF.

---

# 🛒 Parte 1 — Catálogo de Produtos

Nesta primeira parte, foi desenvolvido um catálogo de produtos utilizando uma **lista** para armazenar os produtos e uma combinação de **dicionário e tupla** para representar suas informações.

Cada produto possui:

* **Código**
* **Nome**
* **Preço**

A estrutura escolhida para armazenar código e nome foi uma **tupla**, considerando que essas informações devem permanecer fixas após o cadastro. Já o preço foi armazenado separadamente no dicionário, permitindo sua alteração posteriormente.

Essa organização segue a proposta apresentada no enunciado, que solicita uma estrutura adequada para representar os dados fixos do produto e uma forma de armazenar o preço de maneira atualizável.

## 🔧 Funções desenvolvidas

### `adicionar_produto_catalogo()`

Responsável por adicionar um novo produto ao catálogo.

```python
def adicionar_produto_catalogo(catalogo, codigo, nome, preco):
```

O produto é armazenado como um dicionário, contendo uma tupla com código e nome e o preço separado.

### `buscar_produto_por_codigo_catalogo()`

Realiza uma busca no catálogo utilizando o código do produto.

```python
def buscar_produto_por_codigo_catalogo(catalogo, codigo):
```

Caso o produto seja encontrado, seus dados são retornados. Caso contrário, a função retorna `None`.

Essa implementação atende à proposta do exercício de criar uma função capaz de localizar um produto pelo código.

### `listar_todos_produtos()`

Percorre o catálogo e apresenta os produtos cadastrados de forma organizada, exibindo:

* Código
* Nome
* Preço

A função atende à solicitação do enunciado de listar os produtos cadastrados no catálogo.

---

## 📦 Produtos cadastrados

Para testar o funcionamento do catálogo, foram cadastrados quatro produtos:

| Código | Produto          |     Preço |
| ------ | ---------------- | --------: |
| TEN001 | Tenis Adidas     | R$ 199,99 |
| TEN002 | Tenis Nike       | R$ 299,99 |
| TEN003 | Tenis Puma       | R$ 109,99 |
| TEN004 | Tenis MisterCatt | R$ 159,99 |

Também foi realizado um teste de busca pelo código `TEN002`, permitindo verificar o funcionamento da função de pesquisa.

---

## 🧠 Conceitos praticados

Durante o desenvolvimento desta parte da atividade foram trabalhados os seguintes conceitos:

* Listas
* Tuplas
* Dicionários
* Funções
* Estruturas de repetição
* Busca de dados
* Retorno de valores
* Organização de dados
* Formatação de saída
* Manipulação de estruturas de dados

A atividade também trabalha a escolha adequada das estruturas de dados e a criação de funções com nomes descritivos, conforme os critérios de avaliação apresentados pela faculdade.

---

## ▶️ Como executar

É necessário ter o **Python 3** instalado no computador.

Execute o arquivo pelo terminal:

```bash
python exercicio.py
```

Ou, caso o sistema utilize o comando `python3`:

```bash
python3 exercicio.py
```

O programa apresentará no terminal o resultado da busca pelo produto e, em seguida, a listagem completa do catálogo.

---

## 📄 Enunciado

O enunciado original da atividade está disponível neste repositório em formato PDF para consulta.

**Arquivo:** `enunciado.pdf`

---

## 🎯 Objetivo

O objetivo desta atividade é desenvolver a capacidade de utilizar diferentes estruturas de dados em Python para representar e manipular informações de maneira organizada, aplicando conceitos fundamentais de **Algoritmos e Estrutura de Dados**.

> **Observação:** Este README descreve a implementação realizada neste arquivo Python, correspondente à Parte 1 — Catálogo de Produtos.
