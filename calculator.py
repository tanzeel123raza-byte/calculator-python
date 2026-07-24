import math

while True:
    print("For Addition(+) choose 1")
    print("For Subtraction(-) choose 2")
    print("For Multiplication(*) choose 3")
    print("For Division(/) choose 4")
    print("For Exit choose 5")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        x = float(input("Enter your number: "))
        y = float(input("Etner your number: "))
        print("answer= ", x+y)

    elif choice == 2:
        x = float(input("Enter your number: "))
        y = float(input("Etner your number: "))
        print("asnwer= ", x-y)

    elif choice == 3:
        x = float(input("Enter your number: "))
        y = float(input("Etner your number: "))
        print("answer= ", x*y)

    elif choice == 4:
        x = float(input("Enter your number: "))
        y = float(input("Etner your number: "))
        if y == 0:
            print("Y can't be 0")
        else:
            print("answer= ", x/y)

    elif choice == 5:
        print("No more calculations")
        break

    else:
        print("Invalid operator")