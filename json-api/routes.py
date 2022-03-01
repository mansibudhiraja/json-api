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
    tags = request.args.get("tag")
    sortBy = request.args.get("sortBy")
    direction= request.args.get("direction")
    try:
        all_unique_posts = get_all_posts(tags, sortBy, direction)
        return jsonify({"posts": all_unique_posts}), 200
    except ValueError as err:
        message = str(err)
        return jsonify({"error": message}), 400
   




    




