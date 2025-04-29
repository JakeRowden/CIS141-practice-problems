#Prompts user for bank balance. If balance is less than $100 prints True, otherwise prints False

balance = int(input("What is your bank balance?"))

if balance < 100:
    print("True")
else:
    print("False")
