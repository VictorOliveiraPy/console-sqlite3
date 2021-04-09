import create_product
import delete_product


def main():
    print('--------------------------------------------')
    print(''' ------ MENU INICIAL -----
    Ola. Selecione a ação que deseja executar: 
    [1] Criar novo produto
    [2] Editar um produto já existente
    [3] Listar todos os produtos
    [4] Deletar um produto ''')

    choice = int(input('Digite o número escolhido: '))

    if choice == 1:
        create_product
    elif choice == 2:
        print("funcao n pronta")
    elif choice == 3:
        create_product.show_all_products()


main()
