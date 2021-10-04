import core
from requests import post


@core.poll
def greeting(message):
    core.do("sendMessage", {"chat_id": message['message']['sender_chat']['id'], "text": "test"})
    print("[INFO] Polling system works fine")
