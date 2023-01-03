import requests


#for x in range(0,101):
#    url = 'http://178.62.88.144:31996/profile/api.php/profile/'
#    r = requests.get(url + str(x) , timeout=55)
#    print(r.content)

for x in range(0,101):
    url = 'http://68.183.46.213:30463/settings.php'
    cookies_dict = {"PHPSESSID":"28pc22jfl37506i1u9reb2o0l7","uid": "x"}
    r = requests.get(url + str(x) , timeout=55, cookies=cookies_dict)
    print(r.content)

#Cookie: PHPSESSID=28pc22jfl37506i1u9reb2o0l7; uid=74
#cookies_dict = {"my_cookie": "cookie_value"}
#response = requests.get("http://httpbin.org/cookies", cookies=cookies_dict)
