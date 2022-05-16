#!/usr/bin/python3
'''Script that starts a Flask web application'''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def storage_close(self):
    '''After each request you must remove the current SQLAlchemy Session '''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states():
    st = storage.all(State).values()
    return render_template('7-states_list.html', st=st)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
