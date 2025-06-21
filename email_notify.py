import os
import smtplib
from email.mime.text import MIMEText

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_TO_ADDRESS = os.environ.get("EMAIL_TO_ADDRESS")

def send_email_notify(subject, body):
    if not all([EMAIL_ADDRESS, EMAIL_PASSWORD, EMAIL_TO_ADDRESS]):
        print("SMTP環境変数が設定されていません。")
        return

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_TO_ADDRESS

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
    except Exception as e:
        print(f"メール送信失敗: {e}")
