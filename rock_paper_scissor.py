import random

options = ("Rock", "Paper", "Scissor")

running = True

while running:

    player = None
    computer = random.choice(options)
    while player not in options:
            player = input("Enter your choice (Rock, Paper, Scissor): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's tie")

    elif player == "Rock" and computer == "Paper":
        print("player lost")

    elif player == "Rock" and computer == "Scissor":
        print("player won")

    elif player == "Paper" and computer == "Rock":
        print("player won")

    elif player == "Paper" and computer == "Scissor":
        print("player lost")

    elif player == "Scissor" and computer == "Rock":
        print("player lost")

    elif player == "Scissor" and computer == "Paper":
        print("Player won")

    play_again = input("Again ..?(y/n): ").lower()
    if not play_again == "y":
        running = False


print("Thanks for playing")