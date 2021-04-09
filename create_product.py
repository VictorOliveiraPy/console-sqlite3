import os
products = []

def create():
    
    create_new()

    opcao = 1
    while opcao != 2:
        print('------------------------')
        print(''' Informe a sua ação:
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

    count = 0

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
    show_all_products()

def show_all_products():
    print(products)


create()




