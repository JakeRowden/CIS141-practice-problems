#A program that prompts for 2 numbers then outputs addittion, subtaction, multiplication, division of the first number by second number

#Prompting the user for two numbers
first_number = float(input("Please enter a number"))
second_number = float(input("Please enter another number"))

#Printing the calculations to the terminal and rounded to decrease likelyhood of rounding errors
print(f"{first_number + second_number:.2f}")
print(f"{first_number - second_number:.2f}")
print(f"{first_number * second_number:.2f}")
print(f"{first_number /second_number:.2f}")
