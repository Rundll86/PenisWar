import flask
from file import *
from api import *
from response import *

app = flask.Flask(__name__)
api_list = list(ApiResponse.__dict__.keys())


@app.route("/api", methods=["POST"])
def login():
    arg = flask.request.json
    if arg["type"] in api_list:
        return ApiResponse.__dict__[arg["type"]](arg["data"])
    else:
        return create_response(False, "api not found")


app.run("0.0.0.0", 8080)
