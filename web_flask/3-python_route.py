#!/usr/bin/python3
"""Flask web application"""
from flask import Flask, escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """Displays C with a message in the URL"""
    return "C %s" % escape(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    """Displays Python with a message in the URL"""
    return "Python %s" % escape(text.replace("_", " "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
