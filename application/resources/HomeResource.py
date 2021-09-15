from application.helper.base.Resource import BaseResource

from flask import jsonify


class Home(BaseResource):

    def get(self):
        from application.helper.flask_extras.extras import path
        from application.settings import SERVER_ADDRESS,SERVER_PORT
        home = f"http://{SERVER_ADDRESS}:{SERVER_PORT}"
        return jsonify(
            {
                "About": "This is Flask + SQLAlchemy + Marshmallow + Flask_Restfull Boilerplate Code..",
                "endpoints" : [
                    home+"/",
                    home+path("/")
                ]
            }
        )
