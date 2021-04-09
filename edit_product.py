import csv
import sys
product_id = str (input ('por favor, informe id produto que deseja editar:'))
id =[]
name = []
descrition = []
category = []
price = []
with open('database.txt', 'r') as stream:
    reader = csv.DictReader(stream, delimiter=',')
    count = 0
    for row in reader:
        if row['id'] == product_id:
            option_user = int (input (''' Escolha o item que deseja editar do produto:
            [1] Nome
            [2] Descrição
            [3] Categoria
            [4] Preço
            '''))
            def option1():
                new_input = str (input ( 'informe o nome: '))
                row['nome'] = new_input
                
            def option2():
                new_input = str (input ( 'informe o descrição: '))
                row['descrição'] = new_input

            def option3():
                new_input = str (input ( 'informe o categoria: '))
                row['categoria'] = new_input

            def option4():
                new_input = float (input ( 'informe o preço: '))
                row['preço'] = new_input

            option = { 1:option1, 2:option2, 3:option3, 4:option4}
            option.get(option_user)()
        id.append(row['id'])
        name.append(row['nome'])
        descrition.append(row['descrição'])
        category.append(row['categoria'])
        price.append(row['preço'])
        count += 1
temp = 0
with open('database.txt', mode='w', encoding='utf-8', newline='') as csv_file:
    fieldnames = ["id","nome","descrição","categoria","preço"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for n in id:  
        print(name[temp])
        writer.writerow({"id": id[temp],"nome": name[temp],"descrição": descrition[temp],"categoria": category[temp], "preço": price[temp]})
        temp +=1