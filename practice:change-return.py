print("Please provide a cash amount.")
cents=int(input())
dollars=cents//100
cents=cents-dollars * 100
quarters=cents//25
cents=cents-quarters * 25
dimes=cents//10
cents=cents-dimes * 10
nickels=cents//5
cents=cents-nickels * 5
pennies=cents
print("Dollars: ",dollars)
print("Quarters: ",quarters)
print("Dimes: ",dimes)
print("Nickels: ",nickels)
print("Pennies: ",pennies)
