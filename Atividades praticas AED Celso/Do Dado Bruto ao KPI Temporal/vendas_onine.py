import csv
import json
from datetime import datetime
def carregar_dados_vendas(vendas_online: str) -> list:
    """
    Lê o arquivo CSV de vendas, converte os tipos de dados
    e retorna uma lista de dicionários com as vendas.
    """
    vendas = []

    with open(vendas_online, encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")

        for linha in leitor:
            linha["ValorVenda"] = float(linha["ValorVenda"])
            linha["CustoProduto"] = float(linha["CustoProduto"])
            linha["Data"] = datetime.strptime(
                linha["Data"], "%d/%m/%Y"
            ).date()

            vendas.append(linha)

    return vendas

def calcular_faturamento_lucro_mensal(dados_vendas: list) -> dict:
    """
    Calcula o faturamento e o lucro total de cada mês.

    Complexidade de tempo: O(n), pois a função percorre
    a lista de vendas uma única vez.
    """
    resultado = {}

    for venda in dados_vendas:
        chave_mes = venda["Data"].strftime("%Y-%m")

        if chave_mes not in resultado:
            resultado[chave_mes] = {
                "faturamento": 0.0,
                "lucro": 0.0
            }

        resultado[chave_mes]["faturamento"] += venda["ValorVenda"]
        resultado[chave_mes]["lucro"] += (
            venda["ValorVenda"] - venda["CustoProduto"]
        )

    return resultado

def calcular_variacao_ultimo_mes(
    pilha_historico: list
) -> float | None:
    """
    Calcula a variação percentual do faturamento
    entre os dois últimos meses da pilha.
    """
    if len(pilha_historico) < 2:
        return None

    mes_atual, faturamento_atual = pilha_historico[-1]
    mes_anterior, faturamento_anterior = pilha_historico[-2]

    variacao = (
        (faturamento_atual - faturamento_anterior)
        / faturamento_anterior
    ) * 100

    return variacao

def salvar_sumario_metricas(
    sumario: dict,
    nome_arquivo_json: str
) -> None:
    """
    Salva o resumo das métricas em um arquivo JSON.
    """
    with open(nome_arquivo_json, "w", encoding="utf-8") as arquivo:
        json.dump(
            sumario,
            arquivo,
            ensure_ascii=False,
            indent=4
        )

# --- EXECUÇÃO DO PROGRAMA ---
dados_vendas = carregar_dados_vendas("vendas_online.csv")

for venda in dados_vendas:
    print(venda)


resumo_mensal = calcular_faturamento_lucro_mensal(dados_vendas)

for mes, valores in resumo_mensal.items():
    print(
        f"Mês: {mes} | "
        f"Faturamento: R$ {valores['faturamento']:.2f} | "
        f"Lucro: R$ {valores['lucro']:.2f}"
    )


historico_faturamento_mensal_pilha = []

for mes, valores in resumo_mensal.items():
    historico_faturamento_mensal_pilha.append(
        (mes, valores["faturamento"])
    )

variacao = calcular_variacao_ultimo_mes(
    historico_faturamento_mensal_pilha
)
if variacao is None:
    print("\nNão há dados suficientes para calcular a variação.")
else:
    print(
        f"\nVariação do faturamento entre os últimos meses: "
        f"{variacao:.2f}%"
    )

salvar_sumario_metricas(
    resumo_mensal,
    "resumo_vendas.json"
)
print("\nResumo salvo com sucesso em: resumo_vendas.json")