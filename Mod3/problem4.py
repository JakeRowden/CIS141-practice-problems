'''Prompts the user for: a word, a first index, and a last index. 
Then slices the word at the indexes provided by the user and prints to the screen.'''

#prompts user to input a word, and two indexes
word = input("Provide a word.")
first_index = int(input("Provide the first index you wish to use."))
last_index = int(input("Provide a last index you wish to use."))

#prints the sliced word at those indexes(Inlcuding the index values themselves)
print(word[first_index:last_index+1])
