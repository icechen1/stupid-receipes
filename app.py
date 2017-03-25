from flask import Flask
from recipes import load_recipes

app = Flask(__name__)

@app.route("/")
def hello():
    return str(load_recipes.load())

if __name__ == "__main__":
    app.run()