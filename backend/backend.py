from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Allow only frontend dev server (adjust in production)
CORS(app, origins=["http://localhost:3000"])

@app.get("/ip")
def get_ip():
    return jsonify({
        "ip": request.remote_addr
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
