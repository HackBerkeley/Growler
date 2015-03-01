import sqlite3
import time
from flask import Flask, request, g, render_template

app = Flask(__name__)
DATABASE = 'hakks.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def db_read_hakks():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM hakks")
    return cur.fetchall()

def db_add_hakk(name, hakk):
    cur = get_db().cursor()
    t = str(time.time())
    hakk_info = (name, t, hakk)
    cur.execute("INSERT INTO hakks VALUES (?, ?, ?)", hakk_info)
    get_db().commit()

@app.route("/")
def hello():
    hakks = db_read_hakks()
    print(hakks)
    return render_template('index.html', hakks=hakks)

@app.route("/api/hakk", methods=["POST"])
def receive_hakk():
    print(request.form)
    db_add_hakk(request.form['name'], request.form['hakk'])
    return "Success"

if __name__ == "__main__":
    app.debug = True
    app.run()
