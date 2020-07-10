from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def ping():
    return dict(message="I am running!", ts=datetime.now())


if __name__ == "__main__":
    app.run(host="0.0.0.0")
