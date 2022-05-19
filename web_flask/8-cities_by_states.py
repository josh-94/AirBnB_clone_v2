#!/usr/bin/python3
'''Script that starts a Flask web application and provides cities by state'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_citiesBS():
    """Returns a rendered html template at the /8-cities_by_states route,
    listing all cities"""
    st = storage.all('State').values()
    return render_template('8-cities_by_states.html', st=st)


@app.teardown_appcontext
def close_storage(self):
    '''Removes the current SQLAlchemy Session'''
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
