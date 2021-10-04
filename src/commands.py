from subscription import update
from core import do


@update
def greeting(message):
    do("sendMessage",
       {"chat_id": message['message']['chat']['id'], "text": "Вы сказали: " + message['message']['text']})
    print("[INFO] Polling system works fine")
