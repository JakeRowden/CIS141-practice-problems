# A program that prompts for side lengths of a triangle and computes for the are using Heron's formula and prints the area to the terminal
import math

#Prompting to enter the side lengths of a triangle
length_1 = float(input("Please enter one side length of a triangle"))
length_2 = float(input("please enter another side length of a triangle"))
length_3 = float(input("Please enter a third side length of a triangle"))


#The calculation of a triangle using Herons's formula
semiperimeter = 0.5 * (length_1 + length_2 + length_3)

area = math.sqrt(semiperimeter * (semiperimeter - length_1) * (semiperimeter - length_2) * (semiperimeter - length_3))

#Printing the area of the triangle to the terminal (it is rounded to decrease the likelyhood of loss of precision)
print(f"the area of the triangle is {area:.2f}")
