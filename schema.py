import sqlite3
import create_product
import main

conn = sqlite3.connect('olist_store.db')

cursor = conn.cursor()



cursor.execute("""
CREATE TABLE IF NOT EXISTS category(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    description TEXT NOT NULL
        ); 
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS  product(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    description TEXT NOT NULL,
    value FLOAT NOT NULL,
    FOREIGN KEY (name) REFERENCES category (name)
    );
""")

print('Tabela criada com sucesso.')


def save_dados():
    cursor.execute('INSERT INTO category (name, category, description, valor) VALUES (?,?,?,?)', name, category, description, valor)                  
    conn.commit()


save_dados()




conn.close()
