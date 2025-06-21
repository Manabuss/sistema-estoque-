import sqlite3

def registrar_venda(produto_id, quantidade_vendida):
    """Registra uma venda no banco SQLite e atualiza o estoque."""
    try:
        conn = sqlite3.connect("estoque.db")
        cursor = conn.cursor()

        # Verificar se o produto existe
        cursor.execute("SELECT quantidade, preco_venda FROM produtos WHERE id = ?", (produto_id,))
        produto = cursor.fetchone()

        if produto:
            estoque_atual = produto[0]
            preco_venda = produto[1]

            if estoque_atual >= quantidade_vendida:
                # Atualizar estoque
                novo_estoque = estoque_atual - quantidade_vendida
                cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (novo_estoque, produto_id))

                # Criar tabela de vendas se não existir
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS vendas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    produto_id INTEGER,
                    quantidade INTEGER,
                    total REAL,
                    data TEXT,
                    FOREIGN KEY(produto_id) REFERENCES produtos(id)
                )
                """)

                # Registrar venda
                total_venda = quantidade_vendida * preco_venda
                cursor.execute("INSERT INTO vendas (produto_id, quantidade, total, data) VALUES (?, ?, ?, datetime('now'))",
                               (produto_id, quantidade_vendida, total_venda))

                conn.commit()
                print(f"✅ Venda registrada! Total: R$ {total_venda:.2f}. Estoque atualizado para {novo_estoque}.")
            else:
                print("❌ Estoque insuficiente para essa venda!")

        else:
            print("❌ Erro: Produto não encontrado!")

    except sqlite3.OperationalError as e:
        print(f"❌ Erro operacional no banco de dados: {e}")
    except sqlite3.IntegrityError as e:
        print(f"❌ Erro de integridade no banco de dados: {e}")
    except sqlite3.Error as e:
        print(f"❌ Erro inesperado no banco de dados: {e}")

    finally:
        if conn:
            conn.close()

# Solicitação de venda com validação de entrada
while True:
    entrada_produto = input("Digite o ID do produto vendido: ")
    if entrada_produto.isdigit():
        produto_id = int(entrada_produto)
        break
    else:
        print("❌ Erro: O ID do produto deve ser um número inteiro.")

while True:
    entrada_quantidade = input("Digite a quantidade vendida: ")
    if entrada_quantidade.isdigit():
        quantidade_vendida = int(entrada_quantidade)
        break
    else:
        print("❌ Erro: A quantidade deve ser um número inteiro.")

registrar_venda(produto_id, quantidade_vendida)