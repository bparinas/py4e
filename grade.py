score = input("Enter score between 0.0 - 1.0: ")

try:
    f_score = float(score)
    
    if (f_score < 0.0 or f_score > 1.0) :
       print("Score",f_score,"is out of range")         
except:
       quit()
    

if f_score <= 1.0 and f_score >= 0.9 :
    print("A")
elif f_score >= 0.8 and f_score < 0.9 :
    print("B")
elif f_score >= 0.7 and f_score < 0.8 :
    print("C")
elif f_score >= 0.6 and f_score < 0.7 :
    print("D")
elif f_score < 0.6 and f_score >= 0.0 :
    print("F")
