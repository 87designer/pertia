from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Pertia is Currently in Development"

if __name__ == "__main__":
  app.run()