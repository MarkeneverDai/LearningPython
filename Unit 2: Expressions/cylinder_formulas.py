import math

radius = float(input("Enter radius of cylinder: "))
height = float(input("Enter height of cylinder: "))
area = round(2*math.pi*radius*height+2*math.pi*math.pow(radius,2),2)
volume = round(math.pi*math.pow(radius,2)*height,2)

print("Area =",area)
print("Volume =",volume)
