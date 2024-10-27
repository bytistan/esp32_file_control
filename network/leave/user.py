from flask_socketio import leave_room

from network import socketio
from models import Users 
from database import db

@socketio.on("user$01")
def leave_user(payload):
    try:
        room_name = payload.get("room_name")
        username = payload.get("username")

        if not (room_name and user_id):
            print(colored(f"[!] Invalid data: {payload}", "yellow"))
            return

        user = Users.query.filter_by(username=username).first()
        
        if not user:
            print(colored(f"[!] Record not found", "yellow"))
            return

        print(colored(f"[+] {user.username} connected to : {room_name}", "green"))

        leave_room(room_name)
    except Exception as e:
        print(f"Error handling leave event: {str(e)}")
