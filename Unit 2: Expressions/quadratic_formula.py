import math
a_value = float(input("Enter A value: "))
b_value = float(input("Enter B value: "))
c_value = float(input("Enter C value: "))

x1_solution = (-b_value+math.sqrt(math.pow(b_value,2)-4*a_value*c_value))/(2*a_value)
x2_solution = (-b_value-math.sqrt(math.pow(b_value,2)-4*a_value*c_value))/(2*a_value)

print("x1 = ", x1_solution)
print("x2 = ", x2_solution)