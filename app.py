from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/")
def hello_cs361():
    return "<p>Hello, CS 361!</p>"

@app.route('/getmoves', methods=['POST'])
def getmoves():
    return jsonify(parse_moves(request.get_json()))


def parse_moves(data):
    field = data["field"]
    threshold = data["threshold"]
    moves = data["moves"]

    ret = []
    for move,values in moves.items():
        if values.get(field) <= threshold:
            ret.append(move)


    return json.dumps(ret)