# Calculator for Calculation
# i am taking float input from user so that the calculator can calculate the decimals values as well 
# using try and except method so that the user get a messege to enter a numeric values only 

try:
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    print(f'Addition of {a} and {b} is: {a+b}')
    print(f'Subtraction of {a} and {b} is: {a-b}')
    print(f'Multiplication if {a} and {b} is: {a*b}')
    # Enter only natural number in the 2nd number that is b 
    if b != 0:
        print(f'Division of {a} and {b} is : {a/b}')
    else:
        print(f'Division of {a} and {b} is "Not Defined" ')
except ValueError:
    print("Enter only numeric value ")

    




    