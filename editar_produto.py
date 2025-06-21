import sqlite3

def editar_produto(produto_id, campo, novo_valor):
    """Atualiza um campo específico de um produto no banco SQLite."""
    try:
        conn = sqlite3.connect("estoque.db")
        cursor = conn.cursor()

        # Verificar se o produto existe antes de atualizar
        cursor.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))
        produto = cursor.fetchone()

        if produto:
            cursor.execute(f"UPDATE produtos SET {campo} = ? WHERE id = ?", (novo_valor, produto_id))
            conn.commit()
            print(f"✅ O campo '{campo}' do produto ID {produto_id} foi atualizado para '{novo_valor}'.")
        else:
            print("❌ Erro: Produto não encontrado!")

    except sqlite3.Error as e:
        print(f"❌ Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

# Solicitar dados do usuário para edição
produto_id = int(input("Digite o ID do produto que deseja editar: "))
campo = input("Digite o nome do campo que deseja alterar (ex: nome, categoria, preco_venda, quantidade): ")
novo_valor = input("Digite o novo valor para o campo escolhido: ")

# Se o campo for numérico, converter corretamente
if campo in ["quantidade", "preco_compra", "preco_venda"]:
    novo_valor = float(novo_valor) if "." in novo_valor else int(novo_valor)

editar_produto(produto_id, campo, novo_valor)
