'''
#2. A function called is_palindrome(s) that checks whether a string is a palindrome
(reads the same forward and backward, ignoring case). The function
returns either True or False.
'''
def is_palindrome(s):
    lower_s = s.lower()
    flipped_s = lower_s[::-1]
    return lower_s == flipped_s
    print(flipped_s)
    
print(is_palindrome("dog"))
print(is_palindrome("RAceCar"))
print(is_palindrome("mAdaM"))
