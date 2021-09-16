import os
from dotenv import load_dotenv
from datetime import timedelta
load_dotenv(".env")

APP_VERSION = 'v1.000.0'

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG_MODE = True
MYSQL_ENABLED = False

SERVER_PORT = 7777
SERVER_ADDRESS = '127.0.0.1'
API_VERSION = 'v1'

if MYSQL_ENABLED:
    DATABASE_URI = os.environ.get('DATABASE_URI')
else:
    DATABASE_URI = 'sqlite:///sqlite.db'


def flask_config(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config["JWT_SECRET_KEY"] = SECRET_KEY
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
    app.config['SQLALCHEMY_ECHO'] = False
