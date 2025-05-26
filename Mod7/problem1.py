'''
#1. A function called count_vowels(input) that takes a string
and returns the number of vowels (a, e, i, o, u) in it.
'''
def count_vowels(s):
    v_count = 0
    vowels = "aeiouAEIOU"
    for letter in s:
        if letter in vowels:
            v_count = v_count + 1
    return v_count
    
    
print(count_vowels("LArge"))
print(count_vowels("vowelS"))
print(count_vowels("WarIo"))
print(count_vowels("Salamander"))
    
