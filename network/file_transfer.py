from network import socketio
from models import UploadedFile, Microchips

@socketio.on("file_transfer")
def handle_file_transfer(payload):
    try:
        room_name = payload.get("room_name") 
        microchip_id = payload.get("microchip_id")
        user_id = payload.get("user_id")
            
        piece = payload.get("piece")
        file_name = payload.get("file_name")

        if not (room_name and  microchip_id and user_id):
            print(colored(f"[!] Invalid data: {payload}", "yellow"))
            return 
        
        microchip = Microchips.query.filter(id=microchip_id).first()
        user = Users.query.filter(id=user_id).first()
        
        if not (user and microchip):
            print(colored(f"[!] Record not found.", "yellow"))
            return 
        
        emit("file_transfer", {"piece": piece, "file_name": file_name}, room_name=room_name)
    except Exception as e:
        print(colored(f"[-] Error handling connection event: {str(e)}.", "red"))
