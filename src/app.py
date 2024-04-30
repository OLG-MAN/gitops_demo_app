from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Helm-git-app v0.0.2"