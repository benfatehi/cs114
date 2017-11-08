print("Hello. Please give a distance without units.")
miles=int(input())
print("Now please give me a unit of measurement. Either km, miles, meters, or feet")
unit=input()
print("Now please give me the targeted unit you would like to change your first unit into. Either km, miles, meters, or feet.")
new_unit=input()
if unit=='miles' and new_unit=='km'






km = miles * 1.60934
miles = km * 0.621371
ft = miles * 5280
miles = ft * 0.000189394
m = km * 1000
km = m / 1000
km = ft * 3280.84
ft = km / 3280.84
print (miles , unit , "is " ,  new_unit)
