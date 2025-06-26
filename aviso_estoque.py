import sqlite3

def verificar_estoque_baixo():

conn = sqlite3.connect('estoque_roupas.db')

cursor = conn.cursor()

cursor.execute("""

SELECT nome, quantidade_estoque, estoque_minimo

FROM produtos

WHERE quantidade_estoque <= estoque_minimo

produtos = cursor.fetchall()

conn.close()

print("\n AVISO DE ESTOQUE BAIXO Loja de Roupas\n")

if produtos:

for nome, qtd, minimo in produtos:

else:

print(f"▲ {nome}: {qtd} unidades (mínimo: {minimo})")

print(" Todos os produtos estão acima do estoque mínimo!")

if_name__ == "_main_":

verificar_estoque_baixo()

Faviso_estoque.py