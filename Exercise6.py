correct_password = 12345
# user input 
password = int(input("please enter your password:"))

while correct_password != password:
     #if password is wrong then have to enter again till password is correct 
     password = int(input("Wrong password! Enter your password again: "))

print("Correct! Logging in")