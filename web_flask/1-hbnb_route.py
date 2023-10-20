#!/usr/bin/python3
from flask import Flask

# Create a Flask application
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

if __name__ == '__main__':
    # Running the Flask app on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
