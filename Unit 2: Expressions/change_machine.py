amount = float(input("Total amount? "))
payment = int(input("Cash payment? "))
amount_due = round(payment-amount,2)
print("Change Due: $"+str(amount_due)+"\n")

dollars = amount_due//1
quarters = (amount_due-dollars*1)//0.25
dimes = (amount_due-dollars*1-quarters*0.25)//0.1
nickels = (amount_due-dollars*1-quarters*0.25-dimes*0.1)//0.05
pennies = (amount_due-dollars*1-quarters*0.25-dimes*0.1-nickels*0.05)//0.01

print("Dollars:",dollars,"\n"+"Quarters:",quarters,"\n"+"Dimes:",dimes,"\n"+"Nickels:",nickels,"\n"+"Pennies:",pennies)
