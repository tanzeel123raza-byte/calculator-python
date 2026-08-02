import random
import sys

## A function defined for game of number guessing.

def play_game(max_number):
    """Play one round of the number guessing game."""

    target_number = random.randint(1, max_number)
    attempts = 0

## The main code of game how  it will work. 
    while True:  
        try:
            guess_number = int(input(f"Enter your guess (1-{max_number}):- "))
            if guess_number < 1 or guess_number > max_number:
                print(f"Enter number between 1 to {max_number}. ")
                continue

        except ValueError:
            print("Enter valid integer. ")
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

## this code is here for choosing the level.
while True:

    print("\n===== Number Guessing Game =====")
    print("1. Easy   (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard   (1-500)")
    print("4. Exit")

    difficulty = input("Choose difficulty: ")

    if difficulty == "1":
        play_game(50)

    elif difficulty == "2":
        play_game(100)

    elif difficulty == "3":
        play_game(500)

    elif difficulty == "4":
        print("Thanks for playing!")
        sys.exit()

    else:
        print("Invalid choice.")
        continue

## If you wnat to play again or not.
    while True:
        choice = input("Do you want to play again.. ? (y/n): ").lower()

        if choice == "y":
            break

        elif choice == "n":
            print("Thanks for playing!.. ")
            sys.exit()

        else:
            print("Please enter y or n. ")