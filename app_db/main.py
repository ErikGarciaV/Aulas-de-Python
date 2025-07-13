from db import crud
from InquirerPy import prompt # conheci essa biblioteca através do perfil @aulasdev no tiktok
while True:
    perguntas = [
        {
            "type": "list",
            "name": "acao",
            "message": "escolha uma opção",
            "choices": ["Adicionar usuário", "Listar usuários", "Atualizar usuário", "Deletar usuário", "Sair"]
        },
    ]
    resultado = prompt(perguntas)

    opcao = resultado["acao"]

    match opcao:
        case "Adicionar usuário":
            nome = input("Digite um nome: ")
            idade = int(input("Digite a idade: "))
            crud.adicionar_usuario(nome, idade)
            print("usuario adcionado com sucesso!")

        case "Listar usuários":
            usuarios = crud.listar_usuarios()
            for u in usuarios:
                print(f"ID: {u[0]} | Nome: {u[1]} | Idade: {u[2]}")

        case "Atualizar usuário":
            id_usuario = int(input("escolha o id do usuário: "))
            novo_nome = input("escolha o novo nome do usuário: ")
            nova_idade = int(input("escolha a nova idade do usuário: "))
            crud.atualizar_usuario(id_usuario, novo_nome, nova_idade)
            print("usuário atualizado com sucesso")
            print(crud.listar_usuarios())

        case "Deletar usuário":
            id_usuario = int(input("escolha o id do usuário: "))
            crud.deletar_usuario(id_usuario)
            print("usuario deletado com sucesso")
            print(crud.listar_usuarios())

        case _:
            break