'''
#3. A function called type_advantage(attacker, defender) that takes two Pokémon types as
strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
simple type effectiveness rules. The solution only works for these three sets of input:
print(type_advantage("Water", "Fire")) # "Super Effective"
print(type_advantage("Fire", "Water")) # "Not Very Effective"
print(type_advantage("Electric", "Grass")) # "Neutral"
'''

def type_advantage(attacker, defender):
    if attacker == "Water" and defender == "Fire":
        return "Super Effective"
    if attacker == "Fire" and defender == "Water":
        return "Not Very Effective"
    if attacker == "Electric" and defender == "Grass":
        return "Neutral"
    
print(type_advantage("Water", "Fire"))
print(type_advantage("Fire", "Water"))
print(type_advantage("Electric", "Grass"))
