# Importing necessary libraries
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Render the index.html template for the Pong game
    return render_template("index.html")

if __name__ == "__main__":
    app.run('0.0.0.0',8080)
