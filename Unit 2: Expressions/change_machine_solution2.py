amount = float(input("Total amount? "))
payment = int(input("Cash payment? "))
change = round(payment-amount,2)
print("Change Due $"+str(change))
print()
change = change*100
dollars = change//100
print("Dollars:",dollars)
change = change%100
quarters = change//25
print("Quarters:",quarters)
change = change%25
dimes = change//10
print("Dimes:",dimes)
change = change%10
nickels = change//5
print("Nickels:",nickels)
change = change%5
pennies = change//1
print("Pennies:",pennies)