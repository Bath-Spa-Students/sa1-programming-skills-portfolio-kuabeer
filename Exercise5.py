# 12 months = days 
month_days= {
    1: 31, #jan
    2: 28, #feb
    3: 31, #march
    4: 30, #april
    5: 31, #may
    6: 30, #june
    7: 31, #july
    8: 31, #aug
    9: 30, #sep
    10: 31, #oct
    11: 30, #nov
    12: 31, #dec
}

# user input
month = int(input("please enter a month number: "))

# incorrect
if month > 12 or month < 1:
    print("invalid. Please enter a number between 1 and 12")
# correct 
else:
    days = month_days[month]
    print("The month " + str(month) + " has " + str(days) + " days.")