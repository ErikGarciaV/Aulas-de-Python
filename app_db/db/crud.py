import sqlite3

con = sqlite3.connect("usuarios.db")
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER
)
""")
con.commit()
con.close()

def adicionar_usuario(nome, idade):
    con = sqlite3.connect("usuarios.db")
    cur = con.cursor()
    cur.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))
    con.commit()
    con.close()

def listar_usuarios():
    con = sqlite3.connect("usuarios.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM usuarios")
    usuarios = cur.fetchall()
    con.close()
    return usuarios

def atualizar_usuario(id_usuario, novo_nome, nova_idade):
    con = sqlite3.connect("usuarios.db")
    cur = con.cursor()
    cur.execute("UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?", (novo_nome, nova_idade, id_usuario))
    con.commit()
    con.close()

def deletar_usuario(id_usuario):
    con = sqlite3.connect("usuarios.db")
    cur = con.cursor()
    cur.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    con.commit()
    con.close()
