from flask import Flask
app = Flask(__name__)

@app.route("/")
def base():
    return "<p>It works:)</p>"

@app.route("/healthcheck")
def healthcheck():
    return "<p>Healthcheck</p>"