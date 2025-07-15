from db import session
from sqlalchemy.orm import joinedload
from models.usuario import Usuario

def criar_usuario(nome: str, idade: int) -> Usuario:
    novo = Usuario(nome=nome, idade=idade)
    session.add(novo)
    session.commit()
    session.refresh(novo)
    session.close()
    return novo

def listar_usuarios() -> list[Usuario]:
    usuarios = session.query(Usuario).options(joinedload(Usuario.pedidos)).all()
    session.close()
    return usuarios

def deletar_usuario(usuario_id: int) -> Usuario:
    usuario = session.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        session.close()
        return {"mensagem": "Usuario não encontrado"}
    session.delete(usuario)
    session.commit()
    session.close()
    return {"mensagem": "Usuario Deletado com Sucesso"}
