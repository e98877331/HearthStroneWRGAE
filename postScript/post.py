import requests
import sys
import random

url = ''

if len(sys.argv) == 1:
    url = "http://localhost:9080/logArena"
elif sys.argv[1] == 'server':
    url = "http://hearthstonewr.appspot.com/logArena"

for i in range(1, 10):
    print(url)
    payload = {'roleType': random.randint(0, 8), 'isWin':
               random.choice(['true', 'false']),
               'vsRoleType': random.randint(0, 8)}
    r = requests.post(url, data=payload)
    print(r.text)

#r = requests.get(url)
print(r.text)
