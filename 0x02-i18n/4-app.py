#!/usr/bin/env python3

"""setup a basic Flask app"""

from flask import Flask, render_template
from flask_babel import Babel, request

app = Flask(__name__)
babel = Babel(app)


class Config:
    """config class"""

    LANGUAGES = ["en", "fr"]
    BABEl_DEFAULT_LOCALE = "en"
    BABEl_DEFAULT_TIMEZONE = "UTC"


app.config.from_object("1-app.Config")


@babel.localeselector
def get_locale() -> str:
    """determine the best match languages."""

    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def hello_world() -> str:
    "return page hello world"
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
