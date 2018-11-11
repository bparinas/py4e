hrs = input("Enter Hours:")
rate_per_hr = input("Enter Hourly Rate:")

try:
   f_hrs = float(hrs)
   f_rate = float(rate_per_hr)
except:
   print("Error, please enter numeric input")
   quit()

print(f_hrs, f_rate)   
if f_hrs > 40 :
   ot_hrs = f_hrs - 40
   ot_pay = f_rate * 1.5 * ot_hrs
   gross_pay = ((f_hrs - ot_hrs) * f_rate) + ot_pay
else :
   gross_pay = (f_hrs - ot_hrs) * f_rate

print(str(gross_pay))	
