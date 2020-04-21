#!/usr/bin/python3
"""Flask web application"""
from flask import Flask, escape, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def closes(error):
    """Closes the session"""
    storage.close()


@app.route('/states')
def states():
    """Lists states"""

    states = storage.all('State')

    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def states_id(id):
    """Lists states by id"""

    states = storage.all('State')

    return render_template('9-states.html', states=states, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
