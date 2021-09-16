# -------Installed Packages Import-----
from flask import Flask
from flask_restful import Api
# from flask_jwt_extended import JWTManager
# -------Installed Packages Import-----

# -------App level Imports-----

from application.models import *
from application.settings import SERVER_ADDRESS, SERVER_PORT, SECRET_KEY, DEBUG_MODE,flask_config
from application.database import init_db
from application.routes import urls

# -------App level Imports-----


app = Flask(__name__)
flask_config(app)
api = Api(app)
init_db()
# jwt = JWTManager(app)

urls(api)

if __name__ == "__main__":
    app.run(host=SERVER_ADDRESS, port=SERVER_PORT, debug=DEBUG_MODE)
