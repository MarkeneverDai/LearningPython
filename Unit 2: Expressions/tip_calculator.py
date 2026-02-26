bill = float(input("Enter bill amount: "))
tip_percent = int(input("Percentage to tip: "))
num_people = int(input("Number of people: "))
print()
tip_amount = 0.01*bill*tip_percent
print("Tip amount: $"+str(round(tip_amount,2)))
bill = bill + tip_amount
print("Total amount: $"+ str(round(bill,2)))
print()
tip_amount = tip_amount/num_people
print("Tip per person: $"+ str(round(tip_amount,2)))
bill = bill/num_people
print("Total per person: $"+ str(round(bill,2)))


