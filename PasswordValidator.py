# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# ouput: Valid

password = input("What is your password?: ")
valid = False

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
specialChar = "!@#$%^&*()_+"

capitalCheck = False
numberCheck = False
specialCharCheck = False

letterCounter = 0
for x in password:
    letterCounter += 1
    if x in alphabet[26::]:
        capitalCheck = True
    if x in numbers:
        numberCheck = True
    if x in specialChar:
        specialCharCheck = True
        
if letterCounter > 15 and capitalCheck and numberCheck and specialCharCheck:
    valid = True
    
if valid:
    print("Your password is valid")
else:
    print("Your password is not valid")