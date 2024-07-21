import requests
import time

URL = 'https://jabka.skin/api/jab-tap/frog/tap'
headers = {
    "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjE1NjYyOTEsImV4cCI6MTcyMjE3MTA5MSwicm9sZXMiOlsiUk9MRV9VU0VSIl0sInVzZXJuYW1lIjoiNDYyMzkiLCJpcCI6IjEwOS4yMDcuMTE2LjExNSIsImlkIjo0NjIzOSwic2lkIjoxODIwNjJ9.F5ylxoCM8nGdE0bfudyL2zkB9ncbKQtkEGeaVdbq6R4EqPBVqTVOhnZkgKhK5MA4SKFY7XOEUToM18fhUQSYaoZu7xLYXEsaKbDnG3qfzerQJMNWiCBTinp94xraEoHvBR4a0YW6DBNgTdVH6TyK3CM8natwuNaLmmSHDPSeZcEqYu8ZCglctW6R_Kd93VOl1DyMINaYlR-qfJmTg5ysDRQsNob92TyT_DuLDFt0a332toeygWkBAK4XzehTL8TvXK5tjKDZwfQ6RG_b5vHPsV6N02CmQdFznA297hyWZSHw9Gpu4LVXeyj3OgL75uExRoD-PLjfiEq2MJyN1EIllw"
}
request_body = {'tapsCount': 7}
count = 0
while (count < 4320):
    response = requests.post(URL, json=request_body, headers=headers)
    print(count)
    count -= 7
    time.sleep(0.015)
