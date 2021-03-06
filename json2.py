import urllib.request, urllib.parse, urllib.error
import ssl
import json


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving',url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')


js = json.loads(data)

lst = list()
for item in js["comments"]:
    count = item["count"]
    lst.append(count)

print("Count:", len(lst))
print("Sum:",sum(int(i) for i in lst))
