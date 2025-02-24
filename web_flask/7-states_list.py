#!/usr/bin/python3
""" Script starts a Flask Web Application
listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
import models
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """Displays HTML of all States in Stored Chronologically"""
    states = models.storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(db):
    """Closes or otherwise deallocates resource if it exists"""
    models.storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
