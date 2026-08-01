import random

while True:

    target_number = random.randint(1, 100)
    attempts = 0

    while True:  
        try:
            guess_number = int(input("Enter your guess:- "))
            if guess_number < 1 or guess_number > 100:
                print("Enter number between 1 to 100. ")
                continue

        except ValueError:
            print("Enter the integer in range or valid integer. ")
            continue

        attempts += 1

        if guess_number == target_number:
            print(f"Wow you got this. {target_number}")
            print(f"It took you {attempts} attempts. ")
            break

        elif guess_number > target_number:
            print("Your number is greater than the target. ")

        else:
            print("Your number is less than the target.")

    while True:
        choice = input("Do you want to play again.. ? (y/n): ").lower()

        if choice == "y":
            break

        elif choice == "n":
            print("Thanks for playing!.. ")
            exit()

        else:
            print("Please enter y or n. ")