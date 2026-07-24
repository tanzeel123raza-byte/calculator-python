foods = []
prices = []
total = 0

while True:
    food = input("Enter you'r food to buy or press Quit(Q): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("----Your cart----")

for food in foods:
    print(food, end=" ")

print()
for price in prices:
    total += price

print(f"Your total is: ${total:.2f}")