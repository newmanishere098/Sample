# vulnerable_app.py
import sqlite3

username = input("Username: ")
password = input("Password: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# VULNERABLE: SQL Injection
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

print("Executing:", query)

cursor.execute(query)

result = cursor.fetchone()

if result:
    print("Login successful")
else:
    print("Invalid credentials")