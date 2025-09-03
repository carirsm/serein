from flask import Flask
from .database import db
from config import Config

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable caching for static files

    # setting up to connect to database

    db.init_app(app)

    from . import models
    from .routes import mood_bp
    app.register_blueprint(mood_bp)

    return app