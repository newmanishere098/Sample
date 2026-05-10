import sqlite3

username = input("Username: ")

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# ❌ Vulnerable
query = f"SELECT * FROM users WHERE username = '{username}'"

cursor.execute(query)

print(cursor.fetchall())