import setup
from bottle import post, HTTPResponse, request


@post('/updates')
def updates():
    print(request.json)
    return HTTPResponse(status=200)


def start():
   
