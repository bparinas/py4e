name = input("Enter file:")
handle = open(name)

counts = dict()
for line in handle:
    if not line.startswith("From ") : continue
    words = line.split()
    for word in words:
      counts[word] = counts.get(word,0) + 1

bigcount = None
email = None
for key,value in counts.items():
    #print(key, value)
    if '@' not in key: continue
    if bigcount is None or value > bigcount:
       email = key
       bigcount = value

print(email, bigcount)
