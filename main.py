import requests
import time

URL = 'https://jabka.skin/api/jab-tap/frog/tap'
headers = {
    "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjE1OTMxMTEsImV4cCI6MTcyMjE5NzkxMSwicm9sZXMiOlsiUk9MRV9VU0VSIl0sInVzZXJuYW1lIjoiNDYyMzkiLCJpcCI6IjEwOS4yMDcuMTE2LjExNSIsImlkIjo0NjIzOSwic2lkIjoxOTcxNzl9.6iCOpwTPC0R1uiTmV63QQnyPnZp0kljGO41S6acjZLvcJ-QQ_Ta4i5mjDaUduRIsijZiW8K9GMv7zpmqtR21oXGzNSicqRh-RXDWbzkWWK6kqg9oHTk7wky7YKmDRj53q6YeXBeUcscnRB1YprfaAgq2mN5ps7hJoqctel1VRfd1Wm0C8FMdlZrXDtkpkdTkNsQ9c4K_bW4v_SAqAO-B1kZDv6YRX_XbfkJ_HZlrbLThR83iki_vsrmaQ4ahAD04TPx4MwhvSyLDCQFpvtjwXCABDYvIb7ARnd721t4RS9tXGbhtBCQ2wXPaJsNWYoonPjnU8saxqFTgTMsr_6D6bQ"
}
request_body = {'tapsCount': 7}
count = 0
while (count < 4320):
    response = requests.post(URL, json=request_body, headers=headers)
    print(count)
    count += 7
    time.sleep(0.015)
