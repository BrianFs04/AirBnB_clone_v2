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


@app.route('/cities_by_states')
def cities_by_states():
    """Lists cities by their correspoding states"""

    states = storage.all('State')

    return render_template('8-cities_by_states.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
