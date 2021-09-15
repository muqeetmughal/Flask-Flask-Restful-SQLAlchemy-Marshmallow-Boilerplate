def urls(api):
    from application.helper.flask_extras.extras import path
    from application.resources.HomeResource import Home
    api.add_resource(Home, "/")
