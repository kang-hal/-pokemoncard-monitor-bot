import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0 Safari/537.36"
}

def check_sites():
    for name, url in MONITOR_URLS.items():
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                html = response.text
                if any(keyword in html for keyword in KEYWORDS):
                    message = f"[{name}] キーワード検出: {url}"
                    send_email_notify("ポケカ通知", message)
                    add_to_calendar(name, url)
        except Exception as e:
            print(f"[{name}] エラー: {e}")
