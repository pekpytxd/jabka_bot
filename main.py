import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()
auth_token = os.getenv('TOKEN')

URL = 'https://jabka.skin/api/jab-tap/frog/tap'
headers = {
    "Authorization": auth_token
}
request_body = {'tapsCount': 7}
count = 0
while (count < 5040):
    try:
        response = requests.post(URL, json=request_body, headers=headers)
    except:
        count -= 7
        print("An exception occurred")
    count += 7
    time.sleep(0.015)

print('We are done here!')