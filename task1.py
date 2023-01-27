f = open("recipes.txt", 'r', encoding="utf-8")
cook_book = {}
dishes = []
dish = []

for line in f:
    if line.strip() == "":
        dishes.append(dish)
        dish = []
        continue
    dish.append(line.replace("\n", ""))

k = 0
for dish in dishes:
    cook_book[dish[0]] = []

    for i in range(int(dish[1])):
        ingredient_dict = {}
        dish_words = dish[i + 2].split(" | ")
        ingredient_dict['ingredient_name'] = dish_words[0]
        ingredient_dict['quantity'] = dish_words[1]
        ingredient_dict['measure'] = dish_words[2]
        cook_book[dish[0]].append(ingredient_dict)


for dish in cook_book.items():
    print(dish[0])
    for ingredient in dish[1]:
        print(ingredient)
    print("***")