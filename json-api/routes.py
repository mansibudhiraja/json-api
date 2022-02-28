import json
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def create_route():
    return "<p>Hello World</p>"


