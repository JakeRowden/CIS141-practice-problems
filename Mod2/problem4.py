#A program that prompts for your birth year and prints the two possible ages you can be this year

birth_year = float(input("What is the year you were born?)"))

#If your birthday has happened this year or your birthday is today
age_1 = 2025 - birth_year

#If your birthday has not happened this year 
age_2 = 2025 - birth_year - 1

print(f"You are {age_2:.0f} or {age_1:.0f} years old")
