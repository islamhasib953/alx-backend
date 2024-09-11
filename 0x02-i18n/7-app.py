#!/usr/bin/env python3

"""setup a basic Flask app"""

from flask import Flask, render_template, g
from flask_babel import Babel, request
import pytz
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """config class"""

    LANGUAGES = ["en", "fr"]
    BABEl_DEFAULT_LOCALE = "en"
    BABEl_DEFAULT_TIMEZONE = "UTC"


app.config.from_object("7-app.Config")


@babel.localeselector
def get_locale() -> str:
    """determine the best match languages."""

    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone():
    """Determine the best match TimeZone"""
    timezone = request.args.get("timezone")
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except UnknownTimeZoneError:
            pass
    if g.user and "timezone" in g.user:
        try:
            return pytz.timezone(g.user["timezone"]).zone
        except UnknownTimeZoneError:
            pass
    return app.config["BABEL_DEFAULT_TIMEZONE"]


@app.before_request
def before_request():
    """Function before request"""
    g.user = get_user()


def get_user():
    """Return dictionary of user"""
    if request.args.get("login_as"):
        user = int(request.args.get("login_as"))
        if user in users:
            return users.get(user)
    return None


@app.route("/")
def hello_world() -> str:
    """return page hello world"""
    user_timezone = pytz.timezone(g.user["timezone"])
    current_time = datetime.now(user_timezone).strftime("%Y-%m-%d %H:%M:%S")
    return render_template("7-index.html", current_time=current_time)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
