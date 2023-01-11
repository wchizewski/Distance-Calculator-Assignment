# DISTANCE CALCULATOR ASSIGNMENT

# import
import math

# Title
print("WELCOME TO THE DISTANCE CALCULATOR!")

# Input
x1 = float(input("Enter x1 value: "))
y1 = float(input("Enter y1 value: "))
x2 = float(input("Enter x2 value: "))
y2 = float(input("Enter y2 value: "))

# Process
total = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Answer
print("Distance between the two points is " + str(total) + ".")