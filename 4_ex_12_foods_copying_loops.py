#Rowen Dsa 28-May-2026
#This program was written to learn copying the list
my_foods =['pizza', 'falafel', 'carrot', 'cake']

friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
for foods in my_foods:
    print(foods)

print("\nMy friend's favorite foods are:")
for frd_foods in friend_foods:
    print(frd_foods)