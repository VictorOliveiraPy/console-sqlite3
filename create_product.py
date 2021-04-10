from schema import cursor, conn

products = []


def new_menu():
    while True:
        print('------------------------')
        print(''' Agora você gostaria de:
             [1] Cadastrar mais um produto
             [2] Voltar ao menu inicial / sair do programa  ''')
        opcao = int(input('Digite o numero da sua opcao:  '))
        if opcao == 1:
            create_new()
        else:
            stop_create()


def create_new():
    print(''' Coloque os dados solicitados para fazer o cadastro: ''')
    print('-----------------------------------------')

    name = ({"name": input('Produto: ')})
    description = ({"description": input('Descricao: ')})
    value = ({"value": input('Valor:')})
    category = ({'category': input('Categoria')})

    products.append = {'name': name, 'description': description, 'value': value, 'category': category}


def stop_create():
    print("Finalizando..")


def show_all_products():
    if len(products) == 0:
        print("Você ainda não tem nenhum produto cadastrado")
    else:
        print(products)
