from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

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

POSTGRES_DB = os.getenv("POSTGRES_DB", "postgres")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = 5432

# password comes from Docker secret file (preferred)
POSTGRES_PASSWORD = read_secret("/run/secrets/postgres_password") \
    or os.getenv("POSTGRES_PASSWORD", "unknown")
POSTGRES_USER = read_secret("/run/secrets/postgres_password") \
        or os.getenv("POSTGRES_PASSWORD", "unknown")

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
    app.run(host="0.0.0.0", port=8000, debug=True)
