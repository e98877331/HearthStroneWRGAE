import requests
import sys
import random

url = ''

if len(sys.argv) == 1:
    url = "http://localhost:9080/logArena"
elif sys.argv[1] == 'server':
    url = "http://hearthstonewr.appspot.com/logArena"
elif sys.argv[1] == 'init':
    url = "http://localhost:9080/logArena/init"
    r = requests.post(url)
    print(r.text)
    exit(0)


for i in range(1, 10):
    print(url)
    payload = {'roleType': random.randint(0, 8), 'isWin':
               random.choice(['true', 'false']),
               'vsRoleType': random.randint(0, 8)}
    r = requests.post(url, data=payload)
    print(r.text)

#r = requests.get(url)
#print(r.text)
