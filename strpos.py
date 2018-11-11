text = "X-DSPAM-Confidence:    0.8475";
atpos = text.find(':')
numstr = text[atpos+1:]
print(numstr)
data = float(numstr.strip())
print(data)
