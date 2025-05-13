#A program that asks a user for a number continuously until 0 is entered



while True:
 user_number = input("Enter a number (0 to stop): ")
 user_number_int = int(user_number)

 if user_number_int !=0:
     user_number
     print("You entered " + user_number + "!")
 else:
     break

print("Exiting...")
