
products = dict()
products['id'] = 1 
products['name'] = str(input('Nome: '))


print(''' Escolha uma das categorias abaixo. Digite apenas o numero correspondente a categoria
[1] Alimentos e Bebidas
[2] Vestuario
[3] Moveis e Decoracao
[4] Higiene Pessoal
[5] Acessorios Automotivos
[6] Outros ''')

products['categorie'] = int(input('Categoria: '))
products['description'] = str(input('Descrição: '))
products['price'] = float(input('Preço - R$: '))

print('------------------------')

opcao = 0
print(''' Você deseja cadastrar um novo produto? 
[ 1 ] Sim. Quero cadastrar um produto
[ 2 ] Não. Quero sair do programa. 
''')



# print(products)
