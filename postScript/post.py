import requests
import sys

url = ''

if len(sys.argv) == 1:
    url = "http://localhost:9080/logArena"
elif sys.argv[1] == 'server':
    url = "http://hearthstonewr.appspot.com/logArena"

payload = {'roleType': '2', 'isWin': 'false'}

for i in range(1, 50):
    print(url)
    r = requests.post(url, data=payload)
    print(r.text)

r = requests.get(url)
print(r.text)
