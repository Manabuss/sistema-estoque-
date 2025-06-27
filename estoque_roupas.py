import sqlite3

conn = sqlite3.connect('estoque_roupas.db')

cursor = conn.cursor()

# Criação da tabela

cursor.execute("""

CREATE TABLE IF NOT EXISTS produtos (

")

id INTEGER PRIMARY KEY AUTOINCREMENT,

nome TEXT NOT NULL,

quantidade_estoque INTEGER,

estoque_minimo INTEGER

# Inserindo produtos típicos de loja de roupas

cursor.executemany("""

INSERT INTO produtos (nome, quantidade_estoque, estoque_minimo)

VALUES (?, ?, ?)

[

("Camiseta Branca P", 12, 10),

("Vestido Estampado M", 3, 5),

("Calça Jeans 40", 6, 6),

("Blusa Tricot G", 1, 4),

("Short Saia Preto M", 8, 6),

("Jaqueta Jeans GG", 0, 2)

])

conn.commit()

conn.close()

1 min

print(" Banco de roupas atualizado com sucesso!