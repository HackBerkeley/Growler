from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
import sqlite3
import time
import json
from flask import Flask, request, g, render_template

app = Flask(__name__)
DATABASE = 'growls.db'
counter = 0
websockets = {}

class WSMessage:
    def __init__(self, message):
        self.message = message

    def to_json(self):
        return str(json.dumps(self.message))

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

def db_read_growls():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM growls")
    return cur.fetchall()

def db_add_growl(name, growl):
    cur = get_db().cursor()
    t = str(time.time())
    growl_info = (name, t, growl)
    cur.execute("INSERT INTO growls VALUES (?, ?, ?)", growl_info)
    get_db().commit()

@app.route("/")
def hello():
    growls = db_read_growls()
    return render_template('index.html', growls=growls)

def send_message(message):
    msg = WSMessage(message)
    for id, ws in websockets.items():
        ws.send(msg.to_json())

@app.route('/ws')
def api():
    if request.environ.get('wsgi.websocket'):
        global counter
        ws = request.environ['wsgi.websocket']
        current = counter
        websockets[current] = ws
        counter += 1
        while True:
            message = ws.receive()
            message = json.loads(message)
            db_add_growl(message['name'], message['growl'])
            send_message(message)
        del websockets[current]
        return
    return "No Websocket"

if __name__ == "__main__":
    http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
