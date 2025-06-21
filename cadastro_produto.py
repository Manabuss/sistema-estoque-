import sqlite3

def conectar_banco():
    """Conecta ao banco de dados SQLite e retorna a conexão e o cursor"""
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()
    return conn, cursor

def criar_tabela():
    """Cria a tabela produtos se não existir"""
    conn, cursor = conectar_banco()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT,
        tamanho TEXT,
        cor TEXT,
        quantidade INTEGER,
        preco_compra REAL,
        preco_venda REAL,
        fornecedor TEXT
    )
    """)
    conn.commit()
    conn.close()

def cadastrar_produto():
    """Solicita dados do usuário e cadastra o produto"""
    conn, cursor = conectar_banco()

    try:
        nome = input("Digite o nome do produto: ")
        categoria = input("Digite a categoria: ")
        tamanho = input("Digite os tamanhos disponíveis: ")
        cor = input("Digite a cor: ")
        quantidade = int(input("Digite a quantidade: "))
        preco_compra = float(input("Digite o preço de compra: "))
        preco_venda = float(input("Digite o preço de venda: "))
        fornecedor = input("Digite o fornecedor: ")

        cursor.execute("""
        INSERT INTO produtos (nome, categoria, tamanho, cor, quantidade, preco_compra, preco_venda, fornecedor)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (nome, categoria, tamanho, cor, quantidade, preco_compra, preco_venda, fornecedor))

        conn.commit()
        print(f"✅ Produto '{nome}' cadastrado com sucesso!")

    except sqlite3.Error as e:
        print(f"❌ Erro ao inserir o produto no banco de dados: {e}")

    finally:
        conn.close()

# Executando a função de criação da tabela antes de cadastrar um produto
criar_tabela()
cadastrar_produto()
