
from flask import Flask

app = Flask(__name__)

@app.get("/health")
def health():
    return {"status": "ok"}, 200

@app.get("/crash")
def crash():
    raise RuntimeError("Intentional test error")

@app.get("/")
def index():
    return "OK"



if __name__ == "__main__":
    app.run(debug=False)