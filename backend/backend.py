from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

print("BACKEND PY IS RUNNING")

app = Flask(__name__)
CORS(app)

# -------------------------
# Secrets helper
# -------------------------
def read_secret(path):
    try:
        with open(path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


# -------------------------
# DB config (env + secrets)
# -------------------------

POSTGRES_PORT = 5432
POSTGRES_DB = os.getenv("POSTGRES_DB", "postgres")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")

# password comes from Docker secret file ONLY, or failure.  See docker compose config.
POSTGRES_PASSWORD = read_secret("/run/secrets/POSTGRES_PASSWORD")
POSTGRES_USER = read_secret("/run/secrets/POSTGRES_USER")
if not POSTGRES_PASSWORD: print("Error, docker secrets file failed to read.")
if not POSTGRES_USER: print("Error, docker secrets file failed to read.")

DB_CONFIG = {
    "dbname": POSTGRES_DB,
    "user": POSTGRES_USER,
    "password": POSTGRES_PASSWORD,
    "host": POSTGRES_HOST,
    "port": POSTGRES_PORT,
}


# -------------------------
# DB connection
# -------------------------
def get_conn():
    return psycopg2.connect(**DB_CONFIG)
# -------------------------
# Initialize database
# -------------------------
def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );
    """)

    conn.commit()
    cur.close()
    conn.close()

    print("Database initialized.")

# -------------------------
# Create message
# -------------------------
@app.post("/messages")
def create_message():
    data = request.get_json()
    content = data.get("content")

    if not content:
        return jsonify({"error": "content required"}), 400

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO messages (content) VALUES (%s) RETURNING id;",
        (content,)
    )

    msg_id = cur.fetchone()[0]
    conn.commit()

    cur.close()
    conn.close()

    return jsonify({"id": msg_id, "content": content})


# -------------------------
# Get all messages
# -------------------------
@app.get("/messages")
def get_messages():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id, content, created_at FROM messages ORDER BY id DESC;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify([
        {
            "id": r[0],
            "content": r[1],
            "created_at": r[2].isoformat()
        }
        for r in rows
    ])


# -------------------------
# Run server
# -------------------------
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=8000, debug=True)
    print(app.url_map)
