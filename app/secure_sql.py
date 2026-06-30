import sqlite3
from pathlib import Path


def init_db(db_path="users.db"):
    db_path = Path(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL
        )
    """)

    cursor.execute(
        "INSERT OR IGNORE INTO users (username, email) VALUES (?, ?)",
        ("admin", "admin@correo.com")
    )

    conn.commit()
    conn.close()


def get_user_info(username, db_path="users.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))

    result = cursor.fetchall()
    conn.close()
    return result


if __name__ == "__main__":
    init_db()
    username = input("Enter username: ")
    user_info = get_user_info(username)
    print(user_info)