from bottle import post, HTTPResponse, request
from commands import update
import config


@post('/{}'.format(config.webhook_path))
def updates():
    if config.debug:
        print("[INFO] Received an update:")
        print(request.json)
    for method in update.all.keys():
        if method in request.json:
            update.all[method](request.json)
    return HTTPResponse(status=200)
