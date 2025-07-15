from typing import List
from pydantic import BaseModel, Field
from schemas.pedido import PedidoOutput

class UsuarioInput(BaseModel):
    nome: str = Field(..., min_lengt=2)
    idade: int = Field(..., ge=0, le=150)

class UsuarioOutput(BaseModel):
    id: int
    nome: str
    idade: int
    pedidos: List[PedidoOutput] = []

    class Config:
        from_attributes = True