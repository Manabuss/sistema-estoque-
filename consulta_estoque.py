# consulta_estoque.py

def consultar_por_id(produtos, id_produto):
    for produto in produtos:
        if produto["id"] == id_produto:
            return produto
    return None

def consultar_disponiveis(produtos):
    return [p for p in produtos if p["quantidade"] > 0]

def exibir_produtos(produtos):
    print("\nEstoque Atual:")
    for p in produtos:
        print(f"ID {p['id']}: {p['nome']} ({p['quantidade']} unidades)")

# Exemplo de uso
if __name__ == "__main__":
    estoque = [
        {"id": 101, "nome": "Caneta Azul", "quantidade": 50},
        {"id": 102, "nome": "Caderno", "quantidade": 0},
        {"id": 103, "nome": "Apontador", "quantidade": 12}
    ]

    exibir_produtos(estoque)

    print("\nConsulta por ID 103:")
    produto = consultar_por_id(estoque, 103)
    if produto:
        print(f"Encontrado: {produto['nome']} - {produto['quantidade']} unidades")
    else:
        print("Produto não encontrado.")

    print("\nProdutos disponíveis:")
    disponiveis = consultar_disponiveis(estoque)
    for p in disponiveis:
        print(f"{p['nome']} ({p['quantidade']} unidades)")