from fastapi import APIRouter
from schemas.usuario import UsuarioInput,UsuarioOutput
from services.usuario import criar_usuario, deletar_usuario,listar_usuarios

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.post("/", response_model=UsuarioOutput)
def criar(dados: UsuarioInput):
    return criar_usuario(dados.nome, dados.idade)

@router.get("/", response_model=list[UsuarioOutput])
def listar():
    return listar_usuarios()

@router.delete("/{usuario_id}")
def deletar(usuario_id: int):
    return deletar_usuario(usuario_id)

