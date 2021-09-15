import os
from dotenv import load_dotenv
load_dotenv(".env")

APP_VERSION = 'v1.000.0'

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG_MODE = True
MYSQL_ENABLED = False

SERVER_PORT = 5000
SERVER_ADDRESS = '127.0.0.1'
API_VERSION = 'v1'

if MYSQL_ENABLED:
    DATABASE_URI = os.environ.get('DATABASE_URI')
else:
    DATABASE_URI = 'sqlite:///sqlite.db'

