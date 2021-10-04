import commands
import config
import requests as rq


def start():
    webhook_info_req = rq.get(config.api_url.format(method="getWebhookInfo"))
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
    commands.start()


def get_webhook_url():
    return config.base_url + config.webhook_path


def set_webhook():
    print("[INFO] Starting to set up the webhook")
    setup_request = rq.post(config.api_url.format(method="setWebhook"), json={"url": get_webhook_url()})
    if setup_request.status_code == 200:
        print("[INFO] Webhook setup completed!")
    else:
        print("[ERROR] Webhook setup failed!")
        print(setup_request)


def delete_webhook():
    print("[INFO] Starting to delete webhook")
    delete_request = rq.post(config.api_url.format(method="deleteWebhook"))
    if delete_request.status_code == 200:
        print("[INFO] Webhook deleted successfully")
    else:
        print("[ERROR] Webhook deletion failed!")
        print(delete_request)
