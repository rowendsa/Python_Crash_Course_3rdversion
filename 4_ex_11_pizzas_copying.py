#Rowen Dsa 24-Jun-2024
#This program illustrates the exercise of working with the lists
pizzas = ["pepporoni", "hawaian", "meat lover"]

friend_pizzas = pizzas[:]

pizzas.append("sausage")

friend_pizzas.append("cheese")

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(f"{pizza.title()}")

print("\nMy friend's favorite pizzas are:")
for frd_pizza in friend_pizzas:
    print(f"{frd_pizza.title()}")