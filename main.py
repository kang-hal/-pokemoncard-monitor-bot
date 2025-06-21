from config import MONITOR_URLS, KEYWORDS
from calendar_utils import add_to_calendar
from line_notify import send_line_notify
import requests

def check_sites():
    for name, url in MONITOR_URLS.items():
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                html = response.text
                if any(keyword in html for keyword in KEYWORDS):
                    message = f"[{name}] キーワード検出: {url}"
                    send_line_notify(message)
                    add_to_calendar(name, url)
        except Exception as e:
            send_line_notify(f"[{name}] エラー: {e}")

if __name__ == "__main__":
    check_sites()
