#!/usr/bin/env python3
"""Application Home route"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)


class Config:
    """Configuration class for app and babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/', methods=["GET"])
def home():
    """home route serving the default home page"""
    return render_template("0-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
