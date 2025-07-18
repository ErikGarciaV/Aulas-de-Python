from db import session
from models.usuario import Usuario
from models.pedido import Pedido
from sqlalchemy.orm import joinedload

def criar_usuario(nome, idade):
    novo = Usuario(nome=nome, idade=idade)
    session.add(novo)
    session.commit()
    session.close()

def listar_usuarios():
    usuarios = session.query(Usuario).all()
    session.close()
    return usuarios

def atualizar_usuario(id_usuario, novo_nome, nova_idade):
    
    usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()

    if usuario:
        usuario.nome = novo_nome
        usuario.idade = nova_idade
        session.commit()
        print("Usuario Atualizado com sucesso")
    else:
        print("Usuario não encontrado")

    session.close()

def deletar_usuario(id_usuario):
    
    usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()

    if usuario:
        session.delete(usuario)
        session.commit()
        print("Usuario deletado com sucesso")
    else:
        print("Usuario não encontrado")

    session.close()

def buscar_por_nome(parte_do_nome):
    
    resultado = session.query(Usuario).filter(Usuario.nome.like(f"%{parte_do_nome}%")).all()
    session.close()
    return resultado
   
def criar_pedido(descricao, usuario_id):
    
    pedido = Pedido(descricao=descricao, usuario_id=usuario_id)
    session.add(pedido)
    session.commit()
    session.close()

def listar_pedidos():
    
    pedidos = session.query(Pedido).all()
    for p in pedidos:
        print(f"Pedido #{p.id} - {p.descricao} (Usuário: {p.usuario.nome})")
    session.close()

