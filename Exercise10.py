#function to check num is odd or even 
def number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def main():
    # ask user to enter a number 
    user_number = int(input("Please enter a number: "))
    # to check if its odd or even
    result = number(user_number)
    print(result)
#main function
main()