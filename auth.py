from flask import Blueprint, request, session, jsonify
import sqlite3
import hashlib

auth = Blueprint('auth', __name__)

def hash_pw(password):
    return hashlib.sha256(password.encode()).hexdigest()

@auth.route("/register", methods=["POST"])
def register():
    data = request.json
    conn = sqlite3.connect("trading.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                  (data["username"], hash_pw(data["password"])))
        conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username taken"}), 400
    return jsonify({"message": "Registered"})

@auth.route("/login", methods=["POST"])
def login():
    data = request.json
    conn = sqlite3.connect("trading.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?",
              (data["username"], hash_pw(data["password"])))
    user = c.fetchone()
    if user:
        session["user_id"] = user[0]
        return jsonify({"message": "Logged in"})
    return jsonify({"error": "Invalid credentials"}), 401
