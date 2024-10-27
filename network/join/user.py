from flask_socketio import join_room, emit
from flask import request
from termcolor import colored
from werkzeug.security import check_password_hash

from models import Users
from database import db
from network import socketio

@socketio.on("user$00")
def connect_user(payload):
    try:
        room_name = payload.get("room_name")
        username = payload.get("username")
        password = payload.get("password")

        if not (room_name and user_id and password):
            print(colored(f"[!] Invalid data: {payload}", "yellow"))
            return

        user = Users.query.filter_by(username=username).first()
        
        if not user and not check_password_hash(user.password,password):
            print(colored(f"[!] Record not found", "yellow"))
            return

        print(colored(f"[+] {user.username} connected to : {room_name}", "green"))

        join_room(room_name)
    except Exception as e:
        print(colored(f"[-] Error handling join event: {str(e)}", "red"))
