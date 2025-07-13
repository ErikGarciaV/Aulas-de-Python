
from datetime import datetime,timedelta
agora = datetime.now()
amanha = agora + timedelta(days=1)
dataFormatada = agora.strftime("%d/%m/%Y %H:%M")
print(agora)
print(amanha)
print(dataFormatada) 

import os 
print("diretorio atual:", os.getcwd())
print("arquivos aqui:", os.listdir())

os.mkdir("novaPasta")

from pathlib import Path


pasta = Path("pastaNova")
if not pasta.exists():
    pasta.mkdir()
else:
    print("já existe uma pasta com esse nome")

import random 
numeroAleatorio = random.randint(1, 10)
numeroDigitado = int(input("digite um numero: "))

if numeroDigitado == numeroAleatorio:
    print(f"você digitou o numero {numeroDigitado} e o numero aleatorio gerado foi {numeroAleatorio}, então você acertou!")
else:
    print(f"você digitou o numero {numeroDigitado} e o numero aleatorio gerado foi {numeroAleatorio}, então você errou!")

