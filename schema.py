import sqlite3

conn = sqlite3.connect('olist_store.db')

cursor = conn.cursor()

cursor.execute(
CREATE TABLE category(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL,
        description TEXT NOT NULL
                    ); 
CREATE TABLE product(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL,
        description TEXT NOT NULL,
        value FLOAT NOT NULL,
        FORENKEY (name, name) REFERENCE (category) (name, name)
                    );
                )
print('Table create with sucess')
conn.close()