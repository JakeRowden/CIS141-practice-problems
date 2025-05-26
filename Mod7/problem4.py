'''
#4. A function called ferry_fare(age, vehicle) that calculates the Washington
State Ferry fare based on age and whether the person has a vehicle. Assumes the following rates:
* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
* Children (0-18): Free.
'''

def ferry_fare(age, vehicle):
    if age >= 19 and age <= 64:
        if vehicle == "yes":
            return "$20"
        else:
            return "$10"
    if age >= 65:
        if vehicle == "yes":
            return "$15"
        else:
            return "$5"
    if age < 19:
        return "Free"
    
print(ferry_fare(5, "yes"))
print(ferry_fare(40, "no"))
print(ferry_fare(65, "yes"))
print(ferry_fare(65, "no"))
