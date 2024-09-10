#!/usr/bin/env python3

"""setup a basic Flask app"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """config class"""

    LANGUAGES = ["en", "fr"]
    BABEl_DEFAULT_LOCALE = "en"
    BABEl_DEFAULT_TIMEZONE = "UTC"


app.config.from_object("1-app.Config")


@app.route("/")
def hello_world():
    "return page hello world"
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
