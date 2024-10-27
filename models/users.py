from database import db
from datetime import datetime

class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(2048), nullable=False)
    email = db.Column(db.String(254), nullable=False)

    role = db.Column(db.Integer,nullable=False, default=1)

    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   

    microchip_authorization = db.relationship("MicrochipAuthorization",lazy=True)
    uploaded_file = db.relationship("UploadedFile",lazy=True)
