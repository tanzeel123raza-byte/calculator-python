questions = ("How many bike do you have?: ",
            "which time is not good?: ",
            "The Mt. Everst is located in which country?: ",
            )

options = (("A. 2", "B. 4", "C. 8", "D. 0"),
           ("A. Morning", "B. Evening", "C. Night", "D. Afternoon"),
           ("A. India", "B. Australia", "C. Austria", "D. Pakistan"))

answers = ("D", "D", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+= 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("-----------")
print("RESULT!")
print("-----------")

print("answer: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guess: ", end="")
for guess in guesses:
    print(guess, end=" ")

print()

score = int(score/len(questions)*100)

print(f"Your score is: {score}%")