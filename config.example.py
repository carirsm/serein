import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    # Database configuration, set in your .env file
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # For security, set in your .env file
    SECRET_KEY = os.getenv('SECRET_KEY')

    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'

    # Instructions for new users:
    # 1. Copy this file to your config.py 
    # 2. create an .env file with your database credentials
    # 3. Add your DATABASE_URL and SECRET_KEY to the .env file 