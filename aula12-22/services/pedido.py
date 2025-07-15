from db import session
from models.pedido import Pedido
from models.usuario import Usuario

def criar_pedido(descricao, usuario_id)-> Pedido:
    usuario = session.query(Usuario).filter(Usuario.id == usuario_id).first()

    if not usuario:
        session.close()
        return {"mensagem": "Usuario não encontrado"}
    
    novo = Pedido(descricao=descricao, usuario_id = usuario_id)
    session.add(novo)
    session.commit()
    session.refresh(novo)
    session.close()
    return novo

def listar_pedidos()-> Pedido:
    pedidos = session.query(Pedido).all()
    session.close()
    return pedidos

def deletar_pedido(pedido_id) -> Pedido:
    pedido = session.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        session.close()
        return {"mensagem": "Pedido não encontrado"}
    session.delete(pedido)
    session.commit()
    session.close()
    return {"mensagem": "Pedido deletado com sucesso"}
