#!/usr/bin/env python3

"""setup a basic Flask app"""

from flask import Flask, render_template, g
from flask_babel import Babel, request, format_datetime
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
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(app.Config)


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
            return pytz.timezone(timezone)
        except UnknownTimeZoneError:
            pass
    if g.user and "timezone" in g.user:
        try:
            return pytz.timezone(g.user["timezone"])
        except UnknownTimeZoneError:
            pass
    return pytz.timezone(app.config["BABEL_DEFAULT_TIMEZONE"])


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
    tz = get_timezone()
    current_time = datetime.now(tz)
    formatted_time = format_datetime(current_time, format="medium")
    return render_template("index.html", current_time=formatted_time)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
