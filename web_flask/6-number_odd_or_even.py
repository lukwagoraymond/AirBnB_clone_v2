#!/usr/bin/python3
""" Script starts a Flask Web Application
listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def nisinteger(n):
    """Displays <n> if it is integer"""
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def nisinteger2(n):
    """Displays html page containing <n> if it is integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def nisinteger3(n):
    """Displays html page containing <n> integer is odd or even"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=None)
