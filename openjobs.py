from bs4 import BeautifulSoup
import re
import urllib.request

url = 'file:' + urllib.request.pathname2url(r'c:\My Files\pythonq\jobs.html')
page = urllib.request.urlopen(url)
#soup = BeautifulSoup(page.read())
soup = BeautifulSoup(page, 'html.parser')

#table = soup.find(id="supsystic-table-1")
#table = soup.find('table', id='supsystic-table-1')
#data = soup.find('table')
#print(data)
#rows = table.find_all('tr')
#print(rows)

th = soup.find('th', text='JOB CODE')
data = soup.find_all('th', text='JOB CODE')
print(data)

# The first tr contains the field names.
#headings = [th.get_text() for th in table.find("tr").find_all("th")]

#datasets = []
#for row in table.find_all("tr")[1:]:
#    dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
#    datasets.append(dataset)

#print(datasets)

#for row in soup.find_all('td'):
#   print(row.get())
