import json
from flask import Flask, jsonify, request
from controller.utils import get_all_posts

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/api/ping')
def route_1():
    return jsonify({"success": True}), 200

@app.route("/api/posts")
def get_posts():
    get_all_posts(request)
    return "<p>Hello World</p>"




    




