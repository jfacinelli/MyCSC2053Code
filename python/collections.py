coordinates = (5, 25)
print(coordinates)
x, y = coordinates
print(x, y)
print(coordinates[0])

set1 = {1, 2, 3, 3, 2}
print(set1)
list1 = [1, 2, 2, 3, 3, 4, 4]
list_remove_dups = set(list1)
print(list_remove_dups)

list1 = []
for i in range(50):
    list1.append(i)
print(list1)

list2 = [x for x in range(50) if x > 40]
print(list2)

list_evens = [x for x in range(50) if x % 2 == 0]
list_odds = [x for x in range(50) if x % 2 != 0]
print(list_evens)
print(list_odds)

favorite_foods = {"Kathleen" : "Pizza", "Steve" : "Bugers", "John" : "Chicken"}
favorite_foods["Michelle"] = "Pasta"
favorite_foods["Patrick"] = "Cookies"
print(favorite_foods)

for key, value in favorite_foods.items():
    print(key + "'s favorite food is " + value)

if "Mary" in favorite_foods:
    print("Mary in dictionary")
else:
    favorite_foods["Mary"] = "Cake"

foods = ["Pizza", "Tika Masala", "Pizza", "Bagels", "Bagels", "Ice Cream", "Pizza"]
food_counts = {}
for food in foods:
    if food not in food_counts:
        food_counts[food] = 1
    else:
        food_counts[food] += 1
print(food_counts)

keys = ["one", "two", "three"]
nums = {keys[i] : i + 1 for i in range(len(keys))}
print(nums)