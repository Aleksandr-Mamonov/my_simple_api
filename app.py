from flask import Flask, request
import redis

app = Flask(__name__)
db_redis = redis.Redis(host="redis", port=6379, decode_responses=True)


@app.route("/add", methods=["POST"])
def create_or_update():
    """Accepts body {"key": "value"}, stores it in database and returns created key-value pair.
    If key already exists in database, returns an error message.
    If more than one key:value pair provided, returns an error message."""
    request_body = request.get_json()
    if len(request_body) == 1:
        key = list(request_body.keys())[0]
        if db_redis.exists(key):
            return "This key already exists. Please, provide another key"
        db_redis.mset(request_body)
        return request_body
    else:
        return "Please, provide only one key:value pair in request body."


@app.route("/update", methods=["PUT"])
def update():
    request_body = request.get_json()
    if len(request_body) == 1:
        key = list(request_body.keys())[0]
        if db_redis.exists(key):
            db_redis.mset(request_body)
            return request_body
        return f"No such key in database -> {key}"
    else:
        return "Please, provide only one key:value pair in request body."


@app.route("/get")
def get():
    """Accepts query parameter 'key' and returns corresponding value from database."""
    key = request.args.get("key")
    if key:
        value = db_redis.get(key)
        if value:
            return {key: value}
        else:
            return f"No such key in database -> {key}"
    else:
        return "Please, add a query parameter 'key' to your request"
