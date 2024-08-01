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
while (count <= 750):
    res = requests.post(URL, json=request_body, headers=headers)
    print(res)
    count += 1

print('We are done here!')