import requests
payload = {'roleType' : '2', 'isWin' : 'false'}

for i in range(1,50):
    r= requests.post("http://localhost:9080/logArena",data=payload)


r = requests.get("http://localhost:9080/logArena")
print(r.text)
