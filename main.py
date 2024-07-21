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
while (count < 4320):
    response = requests.post(URL, json=request_body, headers=headers)
    count += 7
    time.sleep(0.02)

print('We are done here!')