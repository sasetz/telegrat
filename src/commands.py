from subscription import subscribe, do, updates


@subscribe
def greeting(message):
    do("sendMessage",
       {"chat_id": message['message']['chat']['id'], "text": "Вы сказали: " + message['message']['text']})
    print("[INFO] Polling system works fine")


def start():
    print("[INFO] Starting to listen")
