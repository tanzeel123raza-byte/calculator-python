import math

def addition(x, y):
    return x+y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x*y

def division(x, y):
    if(y == 0):
        return "Cannot divide  by zero '0'. "
    return x/y

def percentage(x, y):
    if(y == 0):
        return " Cannot divide by zero '0'. "
    return (x/y)*100

def power(x, y):
    return pow(x, y)

def modulus(x, y):
    if(y == 0):
        return "y can't be zero(0). "
    return x % y

def floorDivision(x, y):
    if(y == 0):
        return "Cannot divide by zero '0'. "
    return x//y

def squareRoot(z):
    if(z < 0):
        return "Square root of -ve integer isn't possible"
    return math.sqrt(z)

def getNumber():
    x = float(input("Enter your 1st number: "))
    y = float(input("Enter your 2nd number: "))
    return x, y

def showMenu():
    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percentage")
    print("6. Power")
    print("7. Modulus")
    print("8. Floor Division")
    print("9. Square Root")
    print("10. Show History")
    print("11. Clear History")
    print("12. Exit")

History = []

while True:
        
    try:
        choice = int(input("Enter your choice: "))

        if choice in (1, 2, 3, 4, 5, 6, 7, 8):
            x, y = getNumber()

    except ValueError:
        print("Enter valid integer. ")
        continue

    if choice == 1:
        answer = addition(x, y)
        print("Answer= ", answer)
        History.append(f"{x} + {y} = {answer}")

    elif choice == 2:
        answer = subtraction(x, y)
        print("Answer= ", answer)
        History.append(f"{x} - {y} = {answer}")

    elif choice == 3:
        answer = multiplication(x, y)
        print("Answer= ", answer)
        History.append(f"{x}*{y} = {answer}")

    elif choice == 4:
        answer= division(x, y)
        print("Answer= ", answer)
        History.append(f"{x} / {y} = {answer}")

    elif choice == 5:
        answer = percentage(x, y)
        print("Answer= ", answer)
        History.append(f"({x} / {y}) * {100} = {answer}")

    elif choice == 6:
        answer = power(x, y)
        print("Answer= ", answer)
        History.append(f"{x} ^ {y} = {answer}")

    elif choice == 7:
        answer = modulus(x, y)
        print("Answer= ", answer)
        History.append(f"{x} % {y} = {answer}")

    elif choice == 8:
        answer = floorDivision(x, y)
        print("Answer= ", answer)
        History.append(f"{x} // {y} = {answer}")

    elif choice == 9:
        z = int(input("Enter your number: "))
        answer = squareRoot(z)
        print("Answer= ", answer)
        History.append(f"sqrt({z}) = {answer}")

    elif choice == 10:
        if not History:
            print("No history available.")
        else:
            print("\n---- History ----")
            for item in History:
                print(item)

    elif choice == 11:
        History.clear()
        print("-- History cleared. --")

    elif choice == 12:
        print("Calculation ended. ")
        break

    else:
        print("Invalid choice. ")