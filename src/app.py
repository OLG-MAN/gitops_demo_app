from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "ghcr-helm-app v0.0.1"