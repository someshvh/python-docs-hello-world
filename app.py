from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! my second flask web app"

if __name__ == "__main__":
    app.run()