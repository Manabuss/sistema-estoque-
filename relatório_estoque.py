import sqlite3

2

3

4

conn sqlite3.connect('estoque_roupas.db')

5

cursor conn.cursor()

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

def gerar_relatorio_estoque():

cursor.execute("""

SELECT nome, quantidade_estoque, estoque_minimo

FROM produtos

produtos = cursor.fetchall()

print("\n RELATÓRIO DE ESTOQUE - Loja de Roupas\n")

print("{:<30} {:<10} {:<10} {}".format("Produto", "Qtd", "Mínimo", "Status"))

print("-" * 65)

for nome, qtd, minimo in produtos:

status "▲ Baixo" if qtd <= minimo else " Ok"

print("{:<30} {:<10} {:<10} {}".format(nome, qtd, minimo, status))

conn.close()

if __name__ == "_main_":

gerar_relatorio_estoque