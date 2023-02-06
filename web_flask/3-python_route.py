#!/usr/bin/python3
""" Script starts a Flask Web Application
Web Application listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route1():
    """Displays string below"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_route2():
    """Displays string below"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Display C + space + value in URL"""
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """Display Python + space + value in URL"""
    return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=None)
