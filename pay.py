def computepay(h,r):
  if h > 40 :
     ot_hrs = h - 40
     ot_pay = r * 1.5 * ot_hrs
     gross_pay = ((h - ot_hrs) * r) + ot_pay
  else :
     gross_pay = (h - ot_hrs) * r
    
  return gross_pay 


hrs = input("Enter Hours:")
rate = input("Enter Rate:")

f_hrs = float(hrs)
f_rate = float(rate)

p = computepay(f_hrs, f_rate)
print(str(p))
