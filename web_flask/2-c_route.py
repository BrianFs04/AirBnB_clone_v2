#!/usr/bin/python3
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
    """Displays C followed by a value in text variable"""
    return "C %s" % escape(text.replace("_", " "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
