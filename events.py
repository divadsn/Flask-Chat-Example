from __main__ import socketio
from flask import session, request
from flask_socketio import emit, join_room, leave_room

import random
r = lambda: random.randint(0,255)

# lista zawierająca użytkowników w pokojach czatu
clients = {}


@socketio.on("join", namespace="/chat")
def joined(payload):
    name = session.get("name")
    room = session.get("room")
    join_room(room)

    user = { "id": request.sid, "color": "#%02X%02X%02X" % (r(),r(),r()) }

    if room in clients:
        clients[room][name] = user
    else:
        clients[room] = { name: user }

    emit("status", { "message": session.get("name") + " has entered the room.", "users": clients[room] }, room=room)


@socketio.on("text", namespace="/chat")
def text(payload):
    name = session.get("name")
    room = session.get("room")

    user = clients[room][name]

    # tu ewentualny kod do obróbki wiadomości, typu pogrubienia lub emoji
    message = payload["message"]

    emit("message", { "name": name, "message": payload["message"], "color": user["color"] }, room=room)


@socketio.on("leave", namespace="/chat")
def left(payload):
    name = session.get("name")
    room = session.get("room")
    leave_room(room)

    if room in clients:
        del(clients[room][name])
    else:
        return # ignoruj jeżeli nie był zalogowany
    
    emit("status", { "message": name + " has left the room.", "users": clients[room] }, room=room)