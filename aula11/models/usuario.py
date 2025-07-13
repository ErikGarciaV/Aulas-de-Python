from sqlalchemy import Column, Integer, String
from db import Base

class Usuario(Base):
    __tablename__="usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

    def __repr__(self):
        return f"<Usuario(nome='{self.nome})' idade={self.idade})>"