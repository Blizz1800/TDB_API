import database
from flask import Flask, Response, request
from logging import getLogger


app = Flask(__name__)
logger = getLogger("werkzeug")
logger.disabled = True


@app.route("/")
def root():
    resp = Response()
    resp.data = "XD"
    resp.headers['sex'] = "yes, please"

    return resp


@app.errorhandler(404)
def not_found(error):
    return str(error)


def main():
    db = database.Database()
    db.__init__(True)
    db.init()
    app.run("127.0.0.1", 8001)


if __name__ == "__main__":
    main()
