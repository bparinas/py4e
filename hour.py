name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lst = list()
d = dict()

for line in handle:
    if not line.startswith("From ") : continue
    line = line.split()
    lst = line[5].split(':')

    k = lst[0:1]
    for x in k:
        d[x] = d.get(x,0) + 1

for key,value in sorted(d.items()):
    print(key, value)
