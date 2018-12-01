import re

numlist = list()

name = input("Enter file:")
fh = open(name)

for line in fh:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    #if len(num) != 1 : continue
    if not num : continue
    for x in range(len(num)): 
     #data = int(x)
     numlist.append(num[x])

total = 0
for x in numlist:
    total = total + int(x)
    
print(total)


    #numlist.append(data)

#total = sum(str(numlist))
#print(total)
