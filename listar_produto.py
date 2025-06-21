import sqlite3

def listar_produtos():
    """Lista todos os produtos cadastrados no banco SQLite."""
    try:
        conn = sqlite3.connect("estoque.db")
        cursor = conn.cursor()

        # Buscar todos os produtos
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

        if produtos:
            print("\n📦 **Lista de Produtos**\n")
            for produto in produtos:
                print(f"ID: {produto[0]}")
                print(f"Nome: {produto[1]}")
                print(f"Categoria: {produto[2]}")
                print(f"Tamanho: {produto[3]}")
                print(f"Cor: {produto[4]}")
                print(f"Quantidade: {produto[5]}")
                print(f"Preço de Compra: {produto[6]}")
                print(f"Preço de Venda: {produto[7]}")
                print(f"Fornecedor: {produto[8]}")
                print("-" * 30)
        else:
            print("❌ Nenhum produto cadastrado!")

    except sqlite3.Error as e:
        print(f"❌ Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

# Executa a listagem dos produtos
listar_produtos()