def get_shop_list_by_dishes(used_dishes, person_count):
    shop_dishes_dict = {}
    for used_dish in used_dishes:
        for ingred in cook_book[used_dish]:
            if ingred['ingredient_name'] not in shop_dishes_dict:
                shop_dishes_dict[ingred['ingredient_name']] = {}
                shop_dishes_dict[ingred['ingredient_name']]['measure'] = ingred['measure']
                shop_dishes_dict[ingred['ingredient_name']]['quantity'] = str(int(ingred['quantity']) * person_count)
            else:
                shop_dishes_dict[ingred['ingredient_name']]['quantity'] = str(
                    (int(shop_dishes_dict[ingred['ingredient_name']]['quantity'])
                     + int(ingred['quantity']) * person_count))

    return shop_dishes_dict


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

print("Наша книга рецептов: ")
for dish in cook_book.items():
    print(dish[0])
    for ingredient in dish[1]:
        print(ingredient)
    print("***")

print("############")

shop_dict = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

print("Наш список ингредиентов для покупки: ")
for ingr in shop_dict.items():
    print(ingr)
