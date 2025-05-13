#A simple multiplication table for numbers 1 through 5 made using nested loops. Format your output so each row crresponds to multiplying by a specific output

for i in range(6):
 g=i
 if i != 0:
   continue
    
 for i in range(6):
  if i != 0:
    print("#", i, g+2*i, g+3*i, g+4*i, g+5*i)
