'''Prompts for the user's name and age. Then with String concentation displays what age they are now
and what age they'll be next year'''

#User name and age
name = input("What is your name?")
age = int(input("What is your age?"))


#Calculation
age_this_year_string = str(age)
age_next_year = age + 1
age_next_year_string =str(age_next_year)

#String concentation and print
print("Hello " + name + "! You are " + age_this_year_string + " years old. Next year, you will be " + age_next_year_string + " years old.")
