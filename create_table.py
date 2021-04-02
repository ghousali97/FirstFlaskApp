import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor() #responsible for executing the queries and getting results

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)" #query for creating TABLE
create_item_table = "CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY, name text UNIQUE, price real)"

query_create_item = "INSERT INTO items VALUES (null,?,?)"

cursor.execute(create_table) #creates the file data.db where our database is stored.
cursor.execute(create_item_table)

connection.commit()
connection.close()
