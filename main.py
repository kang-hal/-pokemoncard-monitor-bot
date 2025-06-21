from config import MONITOR_URLS, KEYWORDS
from calendar_utils import add_to_calendar
from email_notify import send_email_notify

def check_sites():
    for name, url in MONITOR_URLS.items():
        try:
            import requests
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                html = response.text
                if any(keyword in html for keyword in KEYWORDS):
                    message = f"[{name}] キーワード検出: {url}"
                    send_email_notify("ポケカ通知", message)
                    add_to_calendar(name, url)
        except Exception as e:
            send_email_notify("ポケカBotエラー", f"[{name}] エラー: {e}")

if __name__ == "__main__":
    check_sites()
