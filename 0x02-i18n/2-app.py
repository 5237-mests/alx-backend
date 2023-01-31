#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DFAULT_TIMEZONE'] = 'UTC' 

babel = Babel(app)


class Config(object):
    """config cls"""
    LANGUAGES = ['en', 'fr']

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(debug=True)