from pathlib import Path

print("seja bem vindo ao gerenciador de arquivos")

def criarPasta(nome):
    pasta = Path(nome)
    if not pasta.exists():
        pasta.mkdir()

criarPasta(nome = input("digite o nome da pasta"))
