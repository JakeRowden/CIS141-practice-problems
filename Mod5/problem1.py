#Prompts the user for an integer n then uses a while loop to sum all integers up to n

n = int(input("Please enter a positvie integer"))
i = 0
g = 0
while i < n:
    i += 1
    g = g+i
    
print(g)
