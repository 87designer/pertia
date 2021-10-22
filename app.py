from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Pertia is currently in development:</h1><p>...Future List of Skills.</p>"