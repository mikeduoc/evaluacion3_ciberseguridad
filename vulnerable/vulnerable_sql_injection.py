
import sqlite3

def get_user_info(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # VULNERABILIDAD: La variable username se inserta directamente en la consulta SQL sin sanitización
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

username = input("Enter username: ")
user_info = get_user_info(username)
print(user_info)
