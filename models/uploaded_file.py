from database import db
from datetime import datetime

class UploadedFile(db.Model):
    __tablename__ = "uploaded_file"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    microchip_id = db.Column(db.Integer, db.ForeignKey("microchips.id"), nullable=False)
    
    successful = db.Column(db.Boolean, nullable=False, default=False)
    
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   

    @classmethod
    def from_dict(cls, data):
        allowed_fields = {"user_id", "microchip_id", "file_path"}
        filtered_data = {key: data[key] for key in allowed_fields if key in data}
        return cls(**filtered_data)
