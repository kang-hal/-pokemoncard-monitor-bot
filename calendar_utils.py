from __future__ import print_function
import datetime
import os.path
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']

def add_to_calendar(title, url):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.utcnow().isoformat() + 'Z'
    event = {
        'summary': f"【ポケカ】{title} 抽選/予約検知",
        'description': f"{url}",
        'start': {'dateTime': datetime.datetime.utcnow().isoformat(), 'timeZone': 'Asia/Tokyo'},
        'end': {'dateTime': (datetime.datetime.utcnow() + datetime.timedelta(hours=1)).isoformat(), 'timeZone': 'Asia/Tokyo'}
    }
    service.events().insert(calendarId='primary', body=event).execute()
