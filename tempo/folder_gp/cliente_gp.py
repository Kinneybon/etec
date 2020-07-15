import os
import time


def carregar_cliente():
    lista = []

    try:
        arquivo = open("cliente.txt", "r")

        for linha in arquivo.readlines():
            coluna = linha.strip().split("#")
            cliente = {
                "nome": coluna[1],
                "razao": coluna[0],
                "cnpj": coluna[2],
                "ie": coluna[3],
                "ata": coluna[4],
                "contrato": coluna[5]
            }
            lista.append(cliente)

        arquivo.close()
    except FileNotFoundError:
        print("Arquivo não existe - Criar....")
        pass

    return lista


def salvar_cliente(lista):
    arquivo = open("cliente.txt", "w")

    for cliente in lista:
        arquivo.write('{}#{}#{}#{}#{}#{}1\n'.format(cliente['razao'], cliente['nome'], cliente['cnpj'], cliente['ie'],
                                                      cliente['ata'], cliente['contrato']))

    arquivo.close()


def existe_cliente(lista, nome):
    if len(lista) > 0:
        for cliente in lista:
            if cliente['nome'] == nome:
                return True
    return False


def adicionar(lista):
    while True:
        nome = input("Digite o nome do cliente: ")

        if not existe_cliente(lista, nome):
            break
        else:
            print("Esse nome já foi utilizado.")
            print("Por favor, digite um novo nome.")
            time.sleep(2)
            os.system("cls")

    cliente = {
        "nome": nome,
        "razao": input("Digite a razão social: "),
        "cnpj": input("Digite o cpnj: "),
        "ie": input("Digite a inscrição estadual: "),
        "ata": input("Digite a ata de assembleia: "),
        "contrato": input("Digite o contrato social: "),
    }
    lista.append(cliente)

    print("O cliente {} foi cadastrado com sucesso!\n".format(cliente['nome']))
    time.sleep(2)
    os.system("cls")


def alterar():
    pass


def excluir():
    pass


def buscar():
    pass


def listar(lista):
    print("Bancos cadastrados: ")
    if len(lista) > 0:
        for i, cliente in enumerate(lista):
            print("Contato {}".format(i + 1))
            print("\tRazao: {}".format(cliente['razao']))
            print("\tNome: {}".format(cliente['nome']))
            print("\tCnpj: {}".format(cliente['cnpj']))
            print("\tIe: {}".format(cliente['ie']))
            print("\tAta: {}".format(cliente['ata']))
            print("\tContrato: {}".format(cliente['contrato']))
            print("===============================================")
        print("Quantidade de Clientes: {}\n".format(len(lista)))
    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")


def principal():
    lista = carregar_cliente()
    while True:
        time.sleep(2)
        os.system("cls")
        print("1 - Cadastrar seu banco")
        print("2 - Sair")
        opcao = int(input("Digite a opção desejada:"))

        if opcao == 1:
            adicionar(lista)
            salvar_cliente(lista)
        elif opcao == 2:
            print("Fechando o programa...")
            exit()
        else:
            print("Opcão inválida, por favor, digite novamente")
            time.sleep(2)
            os.system("cls")


principal()
