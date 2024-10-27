from flask import Flask
from flask_migrate import Migrate

import secrets

import network
import database 

import models

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_hex(16)

database.init_db(app)

migrate = Migrate(app,database.db)

network.socketio.init_app(app)

if __name__ == "__main__":
    network.socketio.run(app, host="0.0.0.0")
