# Use the file name mbox-short.txt as the file name
total = 0
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    num = line[20:]
    total += float(num)
    count += 1
    ave = float(total / count)
print("Average spam confidence:", ave)
