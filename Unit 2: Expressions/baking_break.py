bread_weight = float(input("Enter bread weight(oz): "))
serving_size = float(input("Enter serving size oz per person: "))
num_guests = int(input("Enter number of guests to feed: "))

num_bread = num_guests*serving_size/bread_weight
print()
print("For",num_guests,"people, you will need",num_bread,"loaves of bread:")
print()
print(float(1.5*num_bread),"teaspoons instant yeast.")
print(float(1.5*num_bread),"teaspoons salt.")
print(float(1.5*num_bread),"teaspoons sugar.")
print(float(2.5*num_bread),"teaspoons all-purpose flour.")
print(float(2*num_bread),"teaspoons sourdough starter.")
print(float(0.5*num_bread),"teaspoons lukewarm water.")

