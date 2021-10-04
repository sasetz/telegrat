from bottle import post, HTTPResponse, request
import requests as rq
import config

subscribe_poll = []


def do(method, payload=None):
    request_ = rq.post(config.api_url.format(method=method), json=payload)
    if config.debug and request_:
        print("[INFO] Received a response:")
        print(request_.json())
    elif config.debug:
        print("[WARNING] Request failed")
        print("[WARNING] Status code: {}".format(request_.status_code))
    return request_.json() if request_ else False


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
