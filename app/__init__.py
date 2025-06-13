from flask import Flask
from flask_wtf import CSRFProtect
from .database import db
import config


# creates Flask app and configures it to connect to database + connects SQLAlchemy to it
def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key_here'  # Set a secret key for session management
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable caching for static files

    # csrf = CSRFProtect(app)  # Initialize CSRF protection

   #  @app.context_processor
   # def inject_csrf_token():
    #    from flask_wtf.csrf import generate_csrf
    #    return dict(csrf_token=generate_csrf)

    # setting up to connect to database
    app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from . import models
    from .routes import mood_bp
    app.register_blueprint(mood_bp)

    return app