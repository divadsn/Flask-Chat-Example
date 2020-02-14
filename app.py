import os
import config
from flask import Flask, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from routes import main

app = Flask(__name__, static_url_path="")
app.config.from_object("config")
app.register_blueprint(main)

socketio = SocketIO()
socketio.init_app(app)

import events

if __name__ == "__main__":
    socketio.run(app)