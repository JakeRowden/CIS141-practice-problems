#Prompts the user for a sentence and a word to try to find in that sentence. The program will print true or false

#Input for word and sentence
sentence =input("Please enter a sentence.")
word =input("Please enter a word so I can see if it's in the sentence!")

#prints true/false
print(word in sentence)
