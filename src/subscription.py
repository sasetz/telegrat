from bottle import post, HTTPResponse, request
import config

subscribe_poll = []


@post('/{}'.format(config.webhook_path))
def updates():
    if config.debug:
        print("[INFO] Received an update:")
        print(request.json)
    # for method in update.all.keys():
    #     if method in request.json:
    #         update.all[method](request.json)
    for func in subscribe_poll:
        func(request.json)
    return HTTPResponse(status=200)


def subscribe(func):
    subscribe_poll.append(func)

    def wrapper(message):
        func(message)

    return wrapper
