import sqlite3

def atualizar_valor(produto_id, novo_preco):
    try:
        conn = sqlite3.connect("estoque.db")
        cursor = conn.cursor()

        # Verificar se o produto existe antes de atualizar
        cursor.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))
        produto = cursor.fetchone()

        if produto:
            cursor.execute("UPDATE produtos SET preco_venda = ? WHERE id = ?", (novo_preco, produto_id))
            conn.commit()
            print(f"✅ Preço atualizado para o produto ID {produto_id}.")
        else:
            print("❌ Erro: Produto não encontrado!")

    except sqlite3.Error as e:
        print(f"❌ Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

# Teste a função
produto_id = int(input("Digite o ID do produto que deseja atualizar: "))
novo_preco = float(input("Digite o novo preço de venda: "))

atualizar_valor(produto_id, novo_preco)
