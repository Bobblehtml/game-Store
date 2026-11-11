import sqlite3


def show(rows):
    if not rows:
        print("No games found")
    for game_id, title, genre, price in rows:
        print(game_id, title, "|", genre, "|", f"£{price / 100:.2f}")


def all_games(connection):
    sql = "SELECT id, title, genre, price FROM games ORDER BY title"
    return connection.execute(sql).fetchall()


def find_games(connection, text):
    sql = "SELECT id, title, genre, price FROM games WHERE title LIKE ?"
    return connection.execute(sql, (f"%{text}%",)).fetchall()


if __name__ == "__main__":
    connection = sqlite3.connect("store.db")
    choice = ""
    while choice != "q":
        choice = input("1 All games  2 Search  q Quit: ")
        if choice == "1":
            show(all_games(connection))
        elif choice == "2":
            show(find_games(connection, input("Title contains: ")))
    connection.close()