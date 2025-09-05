import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

class Config:

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        f'sqlite:///{os.path.join(basedir, "serein.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # debug prints
    _secret_key = os.getenv('SECRET_KEY') or 'dev-key-for-testing'
    print(f"Using SECRET_KEY from: {'environment' if os.getenv('SECRET_KEY') else 'fallback'}")

    # dev key: local testing
    SECRET_KEY = _secret_key
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'