import random

target_number = random.randint(1, 100)
attempts = 0

while True:
    guess_number = int(input("Enter your guess:- "))
    attempts += 1
    
    if guess_number == target_number:
        print(f"Wow you got this. {target_number}")
        print(attempts)

    elif guess_number > target_number:
        print("Your number is greater than the target. ")

    else:
        print("Your number is less than the target.")

    