from flask import Flask
from flask sqlalchemy import SQLAlchemy
from .database import db
import config


# creates Flask app and configures it to connect to database + connects SQLAlchemy to it
def create_app():
    app = Flask(__name__)

    # setting up to connect to database
    app.config["SQLALCHEMY)DATABASE_URI"] = config.DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    return app