#!/usr/bin/env python3

"""setup a basic Flask app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    "return page hello world"
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
