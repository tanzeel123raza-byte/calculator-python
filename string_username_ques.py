username = input("Enter your username: ")

if len(username) > 12:
    print("It's not valid username as it contain more than 12 letters. ")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces. ")
elif not username.isalpha():
    print("Your username can't contain numbers. ")
else:
    print(f"Welcome {username}")

