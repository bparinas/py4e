import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
counts = input('Enter count: ')
counts = int(counts)
pos = input('Enter position: ')
pos = int(pos)

tmplst = list()
links = list()
links.append(url)

count = 0

# Retrieve all of the anchor tags
while True:
    data = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(data, 'html.parser')
    tags = soup('a')
    for tag in tags:
        alink = tag.get('href', None)
        alink = str(alink)
        tmplst.append(alink)
    lnk = tmplst[pos-1]
    links.append(lnk)
    tmplst = []
    count += 1
    if count == counts:
        break
    else:
        url = lnk
        continue

for link in links:
    print("Retrieving: ",link)
