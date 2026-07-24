menu = {"Pizaa": 4.64,
        "Burger": 2.99,
        "Noodles": 3.02,
        "Coke": 1.99,
        "Diet coke": 2.45,
        "Pop corn": 5.00,
        "Chicken fry": 4.99,
        "Lemonade": 1.49}

cart = []
total = 0

print("-------MENU-------")
for key, value in menu.items():
    print(f"{key:12}: ${value:.2f}")
print("-------MENU-------")

while True:
    food = input("Select your food or press (q) for quit: ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-------Your order-------")

for food in cart:
    total += menu.get(food)
    print(food)

print()
print(f"Total is: ${total}")


