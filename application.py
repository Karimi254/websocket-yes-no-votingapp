import os
import requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = '{\x1f{\xb1\x06\x8d\x1c\xa1L9\xf8\xe3\xe2\xe2\x98'
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("submit vote")
def vote(data):
    selection = data["selection"]
    emit("announce vote", {"selection": selection}, broadcast=True)


if __name__ == '__main__':
    app.debug = True
    socketio.run(app)
