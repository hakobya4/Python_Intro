recipes_list = []
ingredients_list = []

n = int(input("how many recipes would you like to input: "))


def take_recipe():
    name = str(input("input the name of the recipe: "))
    cooking_time = int(input('input the cooking time of the recipe: '))
    ingredients = input('Enter the ingredients of the recipe: ').split(', ')

    recipe = {'name': name,
              'cooking_time': cooking_time,
              'ingredients': ingredients
              }
    return recipe


for i in range(n):
    recipe = take_recipe()
    for i in recipe['ingredients']:
        if i not in ingredients_list:
            ingredients_list.append(i)
    recipes_list.append(recipe)

for i in recipes_list:
    if i['cooking_time'] < 10 and len(i['ingredients']) < 4:
        i['difficulty'] = 'Easy'
    elif i['cooking_time'] < 10 and len(i['ingredients']) >= 4:
        i['difficulty'] = 'Medium'
    elif i['cooking_time'] > 10 and len(i['ingredients']) < 4:
        i['difficulty'] = 'Intermediate'
    else:
        i['difficulty'] = 'Hard'

    print('Recipe: ', i['name'])
    print('Cooking Time: ', i['cooking_time'])
    print('Ingredients: ', i['ingredients'])
    print('Difficult Level: ', i['difficulty'], '\n')

print('Ingredients available across all recipes: \n')
ingredients_list.sort()
for i in ingredients_list:
    print(i)
