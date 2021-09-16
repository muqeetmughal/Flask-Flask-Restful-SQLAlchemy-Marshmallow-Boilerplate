def create_route(api, resource, path):
    return api.add_resource(resource, path)


def path(url):
    from application.settings import API_VERSION
    # if str(url).endswith("/"):
    #     url = url[-1]
    return '/api/' + API_VERSION + url
