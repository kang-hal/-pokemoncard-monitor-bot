import os
import requests

LINE_TOKEN = os.environ.get("LINE_TOKEN")

def send_line_notify(message):
    if not LINE_TOKEN:
        print("LINE_TOKEN not set.")
        return
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {LINE_TOKEN}"}
    payload = {"message": message}
    requests.post(url, headers=headers, data=payload)
