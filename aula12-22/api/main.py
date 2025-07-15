from fastapi import FastAPI, HTTPException
from db import session, Base, engine
from pydantic import BaseModel, Field
from api import usuarios, pedidos

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(usuarios.router)
app.include_router(pedidos.router)

@app.get("/")
def raiz():
    return {"mensagem": "API está no ar"}
