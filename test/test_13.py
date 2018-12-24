from urllib.request import urlopen
import json

url = " http://py4e-data.dr-chuck.net/comments_166089.json"
html = urlopen(url).read().decode()

info = json.loads(html)

count = 0

for item in info['comments']:
    count = count + int(item['count'])

print('count=', count)