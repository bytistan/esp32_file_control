from database import db
from datetime import datetime

class Microchips(db.Model):
    __tablename__ = "microchips"

    id = db.Column(db.Integer, primary_key=True)

    mac_address = db.Column(db.String(17), nullable=False, unique=True)
    device_name = db.Column(db.Integer, nullable=False)

    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   

    microchip_authorization = db.relationship("MicrochipAuthorization",lazy=True)
    uploaded_file = db.relationship("UploadedFile",lazy=True)
