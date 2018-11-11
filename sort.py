lst = list()
sortlst = list()

fname = input("Enter file name: ")
fh = open(fname)

for line in fh :
  line = line.rstrip()
  lst = line.split()
  for w in lst :
    if w not in sortlst :
      sortlst.append(w)
      continue

sortlst.sort()
print(sortlst)
