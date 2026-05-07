# vulnerable_login.py
# Example of intentionally vulnerable code (for educational/testing purposes only)

import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Username: ")
password = input("Password: ")

# Vulnerable SQL query
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

print("Executing query:")
print(query)

cursor.execute(query)

result = cursor.fetchone()

if result:
    print("Login successful")
else:
    print("Invalid credentials")

conn.close()