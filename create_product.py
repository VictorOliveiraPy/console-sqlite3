import os
import main
products = []

def create():
    
    create_new()

    opcao = 1
    while opcao != 2:
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
    global products
    
    product = {}

    count = 1

    for item in products:
        count += 1

    product['id'] = count
    product['name'] = str(input('Nome: '))

    print(''' Escolha uma das categorias abaixo. Digite apenas o numero correspondente a categoria
    [1] Alimentos e Bebidas
    [2] Vestuario
    [3] Moveis e Decoracao
    [4] Higiene Pessoal
    [5] Acessorios Automotivos
    [6] Outros ''')

  
    product['categorie'] = 0
    while product['categorie'] != 1 and product['categorie'] != 2 and product['categorie'] != 3 and product['categorie'] != 4 and product['categorie'] != 5 and product['categorie'] != 6:

        product['categorie'] = int(input('Categoria: '))

    product['description'] = str(input('Descrição: '))
    product['price'] = float(input('Preço - R$: '))
    
    products.append(product)
  

def stop_create():
    print("Finalizando..")
    main

def show_all_products():
    global products

    if len(products) == 0:
        print("Você ainda não tem nenhum produto cadastrado")
    else:
        print(products)


create()




