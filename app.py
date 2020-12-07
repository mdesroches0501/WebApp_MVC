# app.py - entry point for application

from flask import Flask
app = Flask(__name__)

@app.route("/<name>")
def hello_name(name):
    return "Hello " + name

if __name__ == "__main__":
    Schema()
    app.run(debug=True)
