import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

class Config:
    # SQLite set as fallback for development
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        f'sqlite:///{os.path.join(basedir, "serein.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # debug prints
    SECRET_KEY = os.getenv('SECRET_KEY') or 'dev-key-for-testing'

    # debug mode config
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'