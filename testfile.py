# secure_app.py
#
# A small secure Flask login example demonstrating:
# - Password hashing
# - Parameterized SQL queries
# - Input validation
# - Secure session settings
# - No command execution or unsafe eval usage

from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import re

app = Flask(__name__)

# Strong secret key in production
app.config["SECRET_KEY"] = "change-this-in-production"

# Secure cookie settings
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

DB_NAME = "users.db"


def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def valid_username(username: str) -> bool:
    return bool(re.fullmatch(r"[a-zA-Z0-9_]{3,20}", username))


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username", "").strip()
    password = data.get("password", "")

    if not valid_username(username):
        return jsonify({"error": "Invalid username"}), 400

    if len(password) < 8:
        return jsonify({"error": "Password too short"}), 400

    password_hash = generate_password_hash(password)

    try:
        conn = get_db()

        # SAFE: parameterized query
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password_hash)
        )

        conn.commit()
        conn.close()

        return jsonify({"message": "User registered"}), 201

    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 409


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username", "").strip()
    password = data.get("password", "")

    conn = get_db()

    # SAFE: parameterized query
    user = conn.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    ).fetchone()

    conn.close()

    if user and check_password_hash(user["password"], password):
        session["user"] = username
        return jsonify({"message": "Login successful"})

    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/profile")
def profile():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({
        "username": session["user"]
    })


if __name__ == "__main__":
    init_db()
    app.run(debug=False)