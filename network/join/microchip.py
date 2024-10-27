from flask_socketio import join_room, emit
from flask import request
from werkzeug.security import check_password_hash
from termcolor import colored

from models import Microchips 
from database import db
from network import socketio

@socketio.on("microchip$10")
def connect_microchip(payload):
    try:
        mac_address = payload.get(mac_address)

        if not mac_address and len(mac_address) != 17:
            print(colored(f"Invalid data {payload}", "yellow"))
            return

        microchip = Microchips.query.filter_by(mac_address=mac_address).first()

        if not microchip:
            print(colored(f"[!] Microchip record not found.", "yellow"))
            return
        
        microchip.is_active = True
        db.session.commit()

        join_room(mac_address)
        print(colored(f"[+] Robot connected to room {serial_number}.", "green"))
    except Exception as e:
        print(colored(f"[-] Error handling connection event: {str(e)}.", "red"))
