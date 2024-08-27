#!/usr/bin/env python3
"""Application Home route"""
from flask import Flask, render_template, request, flash
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    """Configuration class for app and babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    SECRET_KEY = "your_secret_key"  # Required for flashing messages


app.config.from_object(Config)
babel = Babel(app)

babel.init_app(app)


@babel.localeselector
def get_locale():
    """Gets the best match language"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', methods=["GET"])
def home():
    """Home route serving the default home page"""
    # flash(_("Hello world"))  # Translatable message
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)
