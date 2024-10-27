from database import db
from datetime import datetime

class MicrochipAuthorization(db.Model):
    __tablename__ = "microchip_authorization"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    microchip_id = db.Column(db.Integer, db.ForeignKey("microchips.id"), nullable=False)

    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   
