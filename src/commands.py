from core import do


def make_poller():
    poller_registry = {}

    def pollers(func, method):
        poller_registry[method] = func
        return func

    pollers.all = poller_registry
    return pollers


update = make_poller()


@update(method="message")
def greeting(message):
    do("sendMessage",
       {"chat_id": message['message']['chat']['id'], "text": "Вы сказали: " + message['message']['text']})
    print("[INFO] Polling system works fine")
