from database import db
from datetime import datetime

class UploadedFile(db.Model):
    __tablename__ = "uploaded_file"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    microchip_id = db.Column(db.Integer, db.ForeignKey("microchips.id"), nullable=False)

    file_path = db.Column(db.String(512), nullable=False, unique=True)
    
    status = db.Column(db.Integer, nullable=True)

    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   
