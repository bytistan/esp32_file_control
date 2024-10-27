from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def init_db(app: Flask):
    app.config.from_object("config.Config")    
    db.init_app(app)

    with app.app_context():
        db.create_all()

"""
Migrate database:

 - flask db init
 - flask db migrate -m "Initial migration"
 - flask db upgrade 
"""
