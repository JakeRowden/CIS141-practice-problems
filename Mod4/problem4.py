#Asks user for age and determines what movies they can watch at a theater based on rating

age = int(input("How old are you"))

if age< 13:
    print("You may watch G rated movies at the theater")

if age >= 13 and age < 18:
    print("You may watch PG-13 and G rated movies at the theater")

if age >= 18:
    print("You may watch R, PG-13, and G rated movies at the theater")
