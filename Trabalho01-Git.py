lst_produtos = []
lst_precos = []
lst_qtd_produtos = []


# Cadastrar
def cadastrar():
    produto = input("Informe o nome do produto: ").upper()
    preco = input("Informe o preço do produto: ")
    qtd = input("Informe a quantidade do produto: ")

    lst_produtos.append(validar_cadastro('nome', produto))
    lst_precos.append(validar_cadastro('preco', preco))
    lst_qtd_produtos.append(validar_cadastro('qtd', qtd))


def validar_cadastro(tipo, valor):
    while True:
        if valor == "" and tipo == "nome":
            print("Favor preencher o nome do produto")
            valor = input("Informe o nome do produto: ").upper()
        elif valor == "" and tipo == "preco":
            print("Favor preencher o preço do produto")
            valor = input("Informe o preço do produto: ")
        elif valor == "" and tipo == "qtd":
            print("Favor preencher a quantidade do produto")
            valor = input("Informe a quantidade do produto: ")
        else:
            print('vai retornar valor pro append', valor)
            return valor


# imprimir produtos da lista
def imprimir():
    print(f'Item - Produto - Preço - Quantidade ')
    for ind, produto in enumerate(lst_produtos):
        print(f'{ind + 1}  --- {produto} ---- {lst_precos[ind]} --- {lst_qtd_produtos[ind]}')


# retirar produtos da lista
def remover():
    imprimir()
    indice = int(input('Remova um produto pelo índice: '))

    if indice > int(len(lst_produtos)):
        input('Indice inválido. -- Tecle Enter')
        remover()
    else:
        lst_produtos.pop(indice - 1)
        lst_precos.pop(indice - 1)
        lst_qtd_produtos.pop(indice - 1)
        print()
        print('Produto retirado com sucesso')


def menu():
    while True:
        escolha = input('''
            Menu
            1. Cadastrar produtos
            2. Imprimir produtos
            3. Retire um dos produtos da lista 

            Escolha: ''')

        print()

        if escolha == '1':
            cadastrar()

        elif escolha == '2':
            imprimir()

        elif escolha == '3':
            remover()

menu()