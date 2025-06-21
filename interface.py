import sqlite3
import tkinter as tk
from tkinter import messagebox

# Conectar ao banco de dados
def conectar_banco():
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT,
        quantidade INTEGER,
        preco REAL
    )
    """)
    conn.commit()
    return conn, cursor

# Funções do sistema
def cadastrar_produto():
    conn, cursor = conectar_banco()
    cursor.execute("INSERT INTO produtos (nome, categoria, quantidade, preco) VALUES (?, ?, ?, ?)",
                   (entry_nome.get(), entry_categoria.get(), int(entry_quantidade.get()), float(entry_preco.get())))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Produto cadastrado!")
    limpar_campos()

def buscar_produto():
    conn, cursor = conectar_banco()
    nome_busca = entry_nome.get()
    cursor.execute("SELECT * FROM produtos WHERE nome LIKE ?", ('%' + nome_busca + '%',))
    resultado = cursor.fetchall()
    conn.close()
   
    mensagem = "\n".join([f"ID: {r[0]}, Nome: {r[1]}, Categoria: {r[2]}, Quantidade: {r[3]}, Preço: R${r[4]:.2f}" for r in resultado]) if resultado else "Nenhum produto encontrado."
    messagebox.showinfo("Resultado da Busca", mensagem)

def atualizar_quantidade():
    conn, cursor = conectar_banco()
    cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (entry_quantidade.get(), entry_id.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Quantidade atualizada!")
    limpar_campos()

def editar_produto():
    conn, cursor = conectar_banco()
    cursor.execute(f"UPDATE produtos SET {entry_campo.get()} = ? WHERE id = ?", (entry_valor.get(), entry_id.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", f"Produto ID {entry_id.get()} atualizado!")
    limpar_campos()

def limpar_campos():
    for entry in [entry_nome, entry_categoria, entry_quantidade, entry_preco, entry_id, entry_campo, entry_valor]:
        entry.delete(0, tk.END)

# Criar janela principal
root = tk.Tk()
root.title("Sistema de Estoque")
root.geometry("400x450")
root.configure(bg="#f0f0f0")  # Cor de fundo da interface

# Criar campos de entrada com texto azul escuro
tk.Label(root, text="Nome do Produto", bg="#f0f0f0", fg="#00008B", font=("Arial", 12, "bold")).pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Categoria", bg="#f0f0f0", fg="#00008B", font=("Arial", 12, "bold")).pack()
entry_categoria = tk.Entry(root)
entry_categoria.pack()

tk.Label(root, text="Quantidade", bg="#f0f0f0", fg="#00008B", font=("Arial", 12, "bold")).pack()
entry_quantidade = tk.Entry(root)
entry_quantidade.pack()

tk.Label(root, text="Preço", bg="#f0f0f0", fg="#00008B", font=("Arial", 12, "bold")).pack()
entry_preco = tk.Entry(root)
entry_preco.pack()

tk.Label(root, text="ID do Produto", bg="#f0f0f0", fg="#00008B", font=("Arial", 12, "bold")).pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Campo para editar", bg="#f0f0f0", fg="#00008B", font=("Arial", 12, "bold")).pack()
entry_campo = tk.Entry(root)
entry_campo.pack()

tk.Label(root, text="Novo Valor", bg="#f0f0f0", fg="#00008B", font=("Arial", 12, "bold")).pack()
entry_valor = tk.Entry(root)
entry_valor.pack()

# Botões com texto azul escuro
tk.Button(root, text="Cadastrar Produto", command=cadastrar_produto, bg="white", fg="#00008B").pack(pady=5)
tk.Button(root, text="Buscar Produto", command=buscar_produto, bg="white", fg="#00008B").pack(pady=5)
tk.Button(root, text="Atualizar Quantidade", command=atualizar_quantidade, bg="white", fg="#00008B").pack(pady=5)
tk.Button(root, text="Editar Produto", command=editar_produto, bg="white", fg="#00008B").pack(pady=5)
tk.Button(root, text="Limpar Campos", command=limpar_campos, bg="white", fg="#00008B").pack(pady=5)

# Iniciar loop da interface
root.mainloop()