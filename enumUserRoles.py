import requests


for x in range(1,51):
    url = 'http://178.62.88.144:31996/profile/api.php/profile/'
    r = requests.get(url + str(x) , timeout=55)
    print(r.content)
