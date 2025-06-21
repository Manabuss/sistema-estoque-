import sqlite3

def atualizar_quantidade(produto_id, nova_quantidade):
    """Atualiza a quantidade de um produto no banco SQLite."""
    try:
        conn = sqlite3.connect("estoque.db")
        cursor = conn.cursor()

        # Verificar se o produto existe antes de atualizar
        cursor.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))
        produto = cursor.fetchone()

        if produto:
            cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_quantidade, produto_id))
            conn.commit()
            print(f"✅ Quantidade do produto ID {produto_id} atualizada para {nova_quantidade}.")
        else:
            print("❌ Erro: Produto não encontrado!")

    except sqlite3.Error as e:
        print(f"❌ Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

# Teste a função
produto_id = int(input("Digite o ID do produto que deseja atualizar: "))
nova_quantidade = int(input("Digite a nova quantidade: "))

atualizar_quantidade(produto_id, nova_quantidade)
