catalogo_loja = []

def adicionar_produto_catalogo(catalogo, codigo, nome, preco):

    produto = {
        "Dados": (codigo, nome),
        "Preço": preco
    }
    catalogo.append(produto)


adicionar_produto_catalogo(catalogo_loja, "TEN001", "Tenis Adidas", 199.99)
adicionar_produto_catalogo(catalogo_loja, "TEN002", "Tenis Nike", 299.99)
adicionar_produto_catalogo(catalogo_loja, "TEN003", "Tenis Puma", 109.99)
adicionar_produto_catalogo(catalogo_loja, "TEN004", "Tenis MisterCatt", 159.99)

def buscar_produto_por_codigo_catalogo(catalogo, codigo):

    for produto in catalogo:
        if produto["Dados"][0] == codigo:
            return produto
            
    return None

produto = buscar_produto_por_codigo_catalogo(catalogo_loja, "TEN002")

if produto is not None:
    print(f"Código: {produto['Dados'][0]} | "
            f"Nome: {produto['Dados'][1]} | "
            f"Preço: R$ {produto['Preço']:.2f}")
else:
    print("Produto não encontrado.")


def listar_todos_produtos(catalogo):

    print("\n--- Catálogo de Produtos ---")
    for produto in catalogo:
        print(
            f"Código: {produto['Dados'][0]} | "
            f"Nome: {produto['Dados'][1]} | "
            f"Preço: R$ {produto['Preço']:.2f}"
        )


listar_todos_produtos(catalogo_loja)