import sqlite3

# Create/connect database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

# Insert sample user
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'secret')")
conn.commit()

# -------------------------
# VULNERABLE LOGIN FUNCTION
# -------------------------
def vulnerable_login(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

    print("Executing Query:")
    print(query)

    cursor.execute(query)

    result = cursor.fetchone()

    if result:
        print("Login successful!")
    else:
        print("Invalid credentials")


# User input
user = input("Username: ")
pwd = input("Password: ")

vulnerable_login(user, pwd)

conn.close()