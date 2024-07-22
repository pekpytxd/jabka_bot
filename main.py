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
while (count < 750):
    requests.post(URL, json=request_body, headers=headers)
    requests.post(URL, json=request_body, headers={"Authorization": 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjE2NTYyOTEsImV4cCI6MTcyMjI2MTA5MSwicm9sZXMiOlsiUk9MRV9VU0VSIl0sInVzZXJuYW1lIjoiNTkzNDkiLCJpcCI6IjEwOS4yMDcuMTE1Ljk0IiwiaWQiOjU5MzQ5LCJzaWQiOjIxNTc0Mn0.mFoaBpsvCX08HKGNtL3X3dYo5V5JdTP4XjXl5Jd-MWkyO_BgcIisYlgYXfvYNoVDkPyUOnfufGoLvEUSuCTygy2bfcFKNvOjCVT6zcBKwVRLmPo5zxYwT92wqsYqxI0M8w0bX5iUvLBQP_7H6wu1bKRdvX3a2SIg0hGkoA9c2OS52FfQMkkj4uooR9XPTydbKZbHmn5QYmHzgbrb_TM-lSP959nJd_xWemLrmelxDQDiuVoKTVxkqYcNqsfTfOQJPAWXJ-CD9kpx1uaSz1UgN2jyOECs_Zg8IBHsJx7jlCpRLF6lH9933LzsjMmcfHiJsg8p27fcSqeBUnzTlOePOw'})
    count += 1
    time.sleep(0.01)

print('We are done here!')