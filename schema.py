import sqlite3

conn = sqlite3.connect('olist_store.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS category(
    id INTEGER  PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    description TEXT NOT NULL
        ); 
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS  product(
    id INTEGER  PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    description TEXT NOT NULL,
    value FLOAT NOT NULL,
    name_id INTEGER,
    FOREIGN KEY (name_id) REFERENCES category(id)
    );
""")

# print('Tabela criada com sucesso.')
