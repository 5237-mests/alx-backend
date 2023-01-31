#!/usr/bin/env python3
"""modul"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """route func"""
    return render_template('0-index.html')


if __name__ == '__main__':
    """main"""
    app.run(debug=True)
