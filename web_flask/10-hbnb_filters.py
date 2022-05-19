#!/usr/bin/python3
'''Script that starts a Flask web application'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def storage_close(self):
    '''After each request you must remove the current SQLAlchemy Session '''
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def display_hbnb():
    '''fetching data from the storage engine FileStorage or DBStorage'''
    st = storage.all(State).values()
    am = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', st=st, am=am)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
