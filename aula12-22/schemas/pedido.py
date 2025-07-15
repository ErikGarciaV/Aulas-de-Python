from pydantic import BaseModel

class PedidoInput(BaseModel):
    descricao: str
    usuario_id: int

class PedidoOutput(BaseModel):
    id: int
    descricao: str
    usuario_id: int

    class Config:
        from_attributes = True