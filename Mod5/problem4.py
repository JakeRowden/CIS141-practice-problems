#A simple multiplication table for numbers 1 through 5 made using nested loops. Format your output so each row crresponds to multiplying by a specific output

for i in range(1,6):
  print("#", end=" ")
  for j in range(1,6):
   
    print(str(j*i) + " ", end='')
   
  print("")
