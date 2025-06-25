import sqlite3

2

←

sistema_estoque

3

4

def excluir_usuario(id_usuario):

5

6

conexao sqlite3.connect('seu_banco.db')

7

cursor conexao.cursor()

8

9

10

11

12

13

14

15

16

's': if confirmacao.lower()

17

18

19

20

else:

# Substitua pelo nome do seu banco de dados

# Verifica se o usuário existe

cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_usuario,))

usuario = cursor.fetchone()

if usuario:

confirmacao = input(

f"Tem certeza que deseja excluir o usuário (usuario[1]} (s/n)? ")

cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))

conexao.commit()

print("Usuário excluído com sucesso!")

21

print("Operação cancelada.")

22

else:

23

print("Usuário não encontrado.")

24

25

conexao.close()

I

26

27

28

# Exemplo de uso:

29

if_name "_main":

30

try:

31

32

33

34

35

id_para_excluir = int(input("Digite o ID do usuário a ser excluído: "))

excluir_usuario(id_para_excluir)

except ValueError:

print("Por favor, insira um número válido.")