import json

from flask import Flask, jsonify, request

from controller.cache import ApiClient
from controller.utils import get_all_posts

app = Flask(__name__)
CACHE_DEFAULT_TIMEOUT_SECONDS = 60
CACHE_DEFAULT_MAX_ENTRIES = 1000

config = {
    "DEBUG": True,  # some Flask specific configs
}

app.config.from_mapping(config)
api_client = ApiClient(CACHE_DEFAULT_MAX_ENTRIES, CACHE_DEFAULT_TIMEOUT_SECONDS)


@app.route("/api/ping")
def handle_ping():
    return jsonify({"success": True}), 200


# This requires tag argument and sortby and direction are optional
# using the cache decorator to cache the results
@app.route("/api/posts")
def get_posts():
    tags = request.args.get("tag") or request.args.get("tags")
    sortby = request.args.get("sortBy")
    direction = request.args.get("direction")

    try:
        all_unique_posts = get_all_posts(api_client, tags, sortby, direction)
        return jsonify({"posts": all_unique_posts}), 200
    except ValueError as err:
        message = str(err)
        return jsonify({"error": message}), 400
