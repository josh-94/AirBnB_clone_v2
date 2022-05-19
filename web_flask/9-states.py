#!/usr/bin/python3
'''Script that starts a Flask web application'''
from flask import Flask, render_template, escape
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def storage_close(self):
    '''After each request you must remove the current SQLAlchemy Session '''
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    st = storage.all(State).values()
    return render_template('9-states.html', st=st, name="None")


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    st = storage.all(State).values()
    for state in st:
        if escape(id) == state.id:
            return render_template('9-states.html', st=state, name=state.name)
    return render_template('9-states.html', st="None", name="None")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
