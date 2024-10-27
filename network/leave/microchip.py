from flask_socketio import leave_room

from network import socketio
from models import Microchips
from database import db

@socketio.on("microchip$11")
def leave_microchip(payload):
    try:
        mac_address = payload.get(mac_address)

        if not mac_address and len(mac_address) != 17:
            print(colored(f"Invalid data {payload}", "yellow"))
            return

        microchip = Microchips.query.filter_by(mac_address=mac_address).first()

        if not microchip:
            print(colored(f"[!] Microchip record not found.", "yellow"))
            return
        
        print(colored(f"[+] Robot connected to room {serial_number}.", "green"))

        microchip.is_active = False 
        db.session.commit()

        leave_room(mac_address)
    except Exception as e:
        print(f"Error handling leave event: {str(e)}")
