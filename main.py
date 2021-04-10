from schema import cursor, conn


def create_new(cursor, conn):
    print(' Coloque os dados solicitados para fazer o cadastro: ')
    print('-----------------------------------------')

    name = ({"name": input('Produto: ')})
    description = ({"description": input('Descricao: ')})
    value = ({"value": input('Valor:')})
    category = ({"Categoria": input('Categoria: ')})

    cursor.execute(f'INSERT INTO product (name, description, value, name_id)'
                   f'VALUES ("{name}", "{description}","{value}","{category}")')
    conn.commit()

    print('PRODUCT REGISTRATION!!!')


def update_obj(cursor, conn):
    cursor = conn.cursor()
    id_name = input('id')
    name = ({"name": input('Produto: ')})
    description = ({"description": input('Descricao: ')})
    value = ({"value": input('Valor:')})

    cursor.execute("""
      UPDATE product
      SET  = ?
      WHERE id = ?
      """, (id_name, name, description, value))

    conn.commit()


def delete(cursor, conn):
    print('enter the product id')
    cursor = conn.cursor()
    id_name = input('id: ')

    cursor.execute("""
    DELETE FROM product
    WHERE id = ?
    """, (id_name,))

    conn.commit()

    print('Record deleted successfully')


def read_data(cursor, conn):
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM product;
    """)

    for linha in cursor.fetchall():
        print(linha)


def main(cursor, conn):
    print('--------------------------------------------')
    print(''' ------ MENU INICIAL -----
    Ola. Selecione a ação que deseja executar: 
    [1] Criar novo produto
    [2] Listar todos os produtos
    [3] Sair
    [4] Deleta produto
    [5] Atualizar produto
     ''')


while True:
    main(cursor, conn)
    choice = input('Digite o número escolhido: ')
    if choice == '1':
        create_new(cursor, conn)
    elif choice == '2':
        read_data(cursor, conn)
    elif choice == '3':
        break
    elif choice == '4':
        delete(cursor, conn)
    elif choice == '5':
        update_obj(cursor,conn)
    else:
        print("Opção Inválida!")
