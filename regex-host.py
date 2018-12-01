import re
msg = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
#x = 'From: Using the : character'
#y = re.findall('^F.+:', x)
#print(y)

#host = re.findall('@(\S+)', msg)
host = re.findall('\S+?@\S+', msg)
print(host)
