#!/usr/bin/env python3
"""Application Home route"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    """home route serving the default home page"""
    return render_template("0-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
