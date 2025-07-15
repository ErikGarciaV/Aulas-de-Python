from fastapi import APIRouter
from schemas.pedido import PedidoInput, PedidoOutput
from services.pedido import criar_pedido,deletar_pedido,listar_pedidos

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.post("/", response_model=PedidoOutput)
def criar(dados: PedidoInput):
    return criar_pedido(dados.descricao, dados.usuario_id)

@router.get("/", response_model= list[PedidoOutput])
def listar():
    return listar_pedidos()

@router.delete("/{pedido_id}")
def deletar(pedido_id: int):
    return deletar_pedido(pedido_id)