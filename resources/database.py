import sqlite3 #imports SQLite3 and links it to the GAMES library
from games_data import GAMES 

connection = sqlite3.connect("store.db") #connects the SQLite3 to the store database
connection.execute("DROP TABLE IF EXISTS games")
connection.execute(""" create table games (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    price INTEGER NOT NULL,
    year INTEGER NOT NULL)""")
connection.executemany(
    "INSERT INTO games (title, genre, price, year) VALUES (?, ?, ?, ?)", GAMES)
connection.commit()
count = connection.execute("SELECT COUNT (*) FROM games").fetchone() [0]
print(count, "games added")
connection.close