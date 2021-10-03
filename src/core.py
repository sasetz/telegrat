import setup
from bottle import post, HTTPResponse, request
import requests as rq

api_url = "https://api.telegram.org/bot" + setup.token + "/{method}"


@post('/{}'.format(setup.webhook_path))
def updates():
    print("[LOG] Received update:")
    print(request.json)
    return HTTPResponse(status=200)


def start():
    webhook_info_req = rq.get(api_url.format(method="getWebhookInfo"))
    print("[INFO] Starting")
    if webhook_info_req.status_code == 200:
        print("[INFO] Webhook check succeeded:")
        print(webhook_info_req.json())
        if not webhook_info_req.json()["url"]:
            print("[INFO] Creating webhook")
            set_webhook()
    else:
        print("[ERROR] Webhook check failed. Creating the webhook anyways")
        set_webhook()


def set_webhook():
    setup_request = rq.post(api_url.format(method="setWebhook"), json={"url": setup.base_url + setup.webhook_path})
    if setup_request.status_code == 200:
        print("[INFO] Webhook setup completed!")
    else:
        print("[ERROR] Webhook setup failed!")
        print(setup_request)
