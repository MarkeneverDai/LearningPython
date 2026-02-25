ozdrank = input("How many ounces of water have you drank today? ")
cup_drank = float(int(ozdrank)/8)
cups_left = int(8-cup_drank)
print("You have",cups_left,"of water to drink today.")