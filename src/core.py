import setup
from bottle import post, HTTPResponse, request
import requests as rq

api_url = "https://api.telegram.org/bot" + setup.token + "/{method}"


def make_poller():
    poller_registry = []

    def pollers(func):
        poller_registry.append(func)
        return func

    pollers.all = poller_registry
    return pollers


poll = make_poller()


@post('/{}'.format(setup.webhook_path))
def updates():
    for func in poll.all:
        func(request.json())
    return HTTPResponse(status=200)


def start():
    webhook_info_req = rq.get(api_url.format(method="getWebhookInfo"))
    print("[INFO] Starting")
    if webhook_info_req.status_code == 200:
        print("[INFO] Webhook check succeeded:")
        print(webhook_info_req.json())
        if not webhook_info_req.json()["result"]["url"]:
            print("[INFO] Creating webhook")
            set_webhook()
        elif webhook_info_req.json()["result"]["url"] != get_webhook_url():
            print("[INFO] Webhook URL mismatched, changing to up-to-date")
            delete_webhook()
            set_webhook()
        else:
            print("[INFO] Webhook is up-to-date")
    else:
        print("[ERROR] Webhook check failed. Creating the webhook anyways")
        set_webhook()


def get_webhook_url():
    return setup.base_url + setup.webhook_path


def set_webhook():
    print("[INFO] Starting to set up the webhook")
    setup_request = rq.post(api_url.format(method="setWebhook"), json={"url": get_webhook_url()})
    if setup_request.status_code == 200:
        print("[INFO] Webhook setup completed!")
    else:
        print("[ERROR] Webhook setup failed!")
        print(setup_request)


def delete_webhook():
    print("[INFO] Starting to delete webhook")
    delete_request = rq.post(api_url.format(method="deleteWebhook"))
    if delete_request.status_code == 200:
        print("[INFO] Webhook deleted successfully")
    else:
        print("[ERROR] Webhook deletion failed!")
        print(delete_request)


def do(method, payload=None):
    request_ = rq.post(api_url.format(method=method), json=payload)
    return request_.json() if request_ else False
