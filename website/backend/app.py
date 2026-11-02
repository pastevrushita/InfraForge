
import os
import socket
from datetime import UTC, datetime

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "InfraForge",
        "message": "InfraForge backend API is running",
        "status": "healthy"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(UTC).isoformat()
    }), 200


@app.route("/api/status")
def status():
    return jsonify({
        "application": "InfraForge",
        "status": "running",
        "environment": os.getenv("APP_ENV", "development"),
        "hostname": socket.gethostname(),
        "timestamp": datetime.now(UTC).isoformat()
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
