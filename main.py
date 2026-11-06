
import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return {"status": "ok"}, 200


@app.get("/crash")
def crash():
    app.logger.error("Intentional test error")
    return jsonify({"status": "error", "message": "Intentional test error"}), 500


@app.get("/")
def index():
    return "OK"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port, debug=False)