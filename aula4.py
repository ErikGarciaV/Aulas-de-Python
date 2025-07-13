
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")

with open("dados.txt", "a") as arquivo:
    arquivo.write(f"{nome},{idade},{cidade}")

with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        nome, idade, cidade = linha.strip().split(",")
        print(f"{nome} tem {idade} anos e mora em {cidade}")