from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Helm-repo-app v0.0.1"