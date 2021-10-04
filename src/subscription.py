from bottle import post, HTTPResponse, request
import config


def make_poller():
    poller_registry = {}

    def pollers(func, method):
        poller_registry[method] = func
        return func

    pollers.all = poller_registry
    return pollers


update = make_poller()


@post('/{}'.format(config.webhook_path))
def updates():
    if config.debug:
        print("[INFO] Received an update:")
        print(request.json)
    for method in update.all.keys():
        if method in request.json:
            update.all[method](request.json)
    return HTTPResponse(status=200)
