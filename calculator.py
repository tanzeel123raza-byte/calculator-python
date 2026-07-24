# import math

def addition(x, y):
    return x+y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x*y

def division(x, y):
    if(y == 0):
        return "Cannot divide  by zero"
    return x/y

def getNumber():
    x = float(input("Enter your 1st number: "))
    y = float(input("Enter your 2nd number: "))
    return x, y

while True:
    try:
        choice = int(input("Enter your choice: "))

        if choice in (1, 2, 3, 4):
            x, y = getNumber()

    except ValueError:
        print("Enter valid integer. Idiot! ")
        continue

    if choice == 1:
        print("Answer= ", addition(x, y))

    elif choice == 2:
        print("Answer= ", subtraction(x, y))

    elif choice == 3:
        print("Answer= ", multiplication(x, y))

    elif choice == 4:
        print("Answer= ", division(x, y))

    elif choice == 5:
        print("Calculation ended. ")
        break

    else:
        print("Invalid choice. ")