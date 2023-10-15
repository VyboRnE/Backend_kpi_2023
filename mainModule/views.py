from flask import Flask
import json, time

app = Flask(__name__)

@app.route("/")
def base():
    return "<p>It works:)</p>"

@app.route("/healthcheck", methods=['GET'])
def healthcheck():
    healthcheck_data = {'Page': 'Healthcheck', 
                        'Status': 'Service is working.',
                        'Time': time.asctime(time.localtime(time.time()))}
    healthcheck_json = json.dumps(healthcheck_data)
    return healthcheck_json, 200