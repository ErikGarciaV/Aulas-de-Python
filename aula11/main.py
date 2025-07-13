from db import Base, engine
import funcoes
from InquirerPy import prompt
from funcoes import criar_usuario, listar_usuarios, atualizar_usuario, deletar_usuario

Base.metadata.create_all(engine)

while True:
    perguntas = [
        {
            "type": "list",
            "name": "acao",
            "message": "escolha uma opção",
            "choices": ["Adicionar usuário", "Listar usuários", "Atualizar usuário", "Deletar usuário", "Buscar usuário", "Sair"]
        },
    ]
    resultado = prompt(perguntas)

    opcao = resultado["acao"]

    match opcao:
        case "Adicionar usuário":
            nome = input("Digite um nome: ")
            idade = int(input("Digite a idade: "))
            funcoes.criar_usuario(nome, idade)
            print("usuario adcionado com sucesso!")

        case "Listar usuários":
            usuarios = funcoes.listar_usuarios()
            for u in usuarios:
                print(f"ID: {u.id} | Nome: {u.nome} | Idade: {u.idade}")

        case "Atualizar usuário":
            id_usuario = int(input("escolha o id do usuário: "))
            novo_nome = input("escolha o novo nome do usuário: ")
            nova_idade = int(input("escolha a nova idade do usuário: "))
            funcoes.atualizar_usuario(id_usuario, novo_nome, nova_idade)
            print("usuário atualizado com sucesso")

        case "Deletar usuário":
            id_usuario = int(input("escolha o id do usuário: "))
            funcoes.deletar_usuario(id_usuario)
            print("usuario deletado com sucesso")

        case "Buscar usuário":
            parte_do_nome = input("Digite uma parte do nome: ")
            usuario = funcoes.buscar_por_nome(parte_do_nome)
            if usuario:
                for u in usuario:
                    print(f"ID: {u.id} | Nome: {u.nome} | Idade: {u.idade}")
            else:
                print("Usuário não encontrado")
        case _:
            break