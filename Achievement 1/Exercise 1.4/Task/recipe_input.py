import pickle


def take_recipe():
    name = str(input("input the name of the recipe: "))
    cooking_time = int(input('input the cooking time of the recipe: '))
    ingredients = input('Enter the ingredients of the recipe: ').split(', ')
    difficulty = calc_difficulty(cooking_time, ingredients)
    recipe = {'name': name,
              'cooking_time': cooking_time,
              'ingredients': ingredients,
              'difficulty': difficulty
              }
    return recipe


def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = 'Easy'
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = 'Medium'
    elif cooking_time > 10 and len(ingredients) < 4:
        difficulty = 'Intermediate'
    else:
        difficulty = 'Hard'
    return difficulty


filename = input("Enter the filename where you've stored recipes: ")
try:
    file = open(filename, 'br')
    data = pickle.load(file)
except FileNotFoundError:
    print("File doesn't exist - exiting.")
    data = {'recipes_list': [], 'all_ingredients': []}
except:
    print("An unexpected error occurred.")
    data = {'recipes_list': [], 'all_ingredients': []}
else:
    file.close()
finally:
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

n = int(input("how many recipes would you like to input: "))
recipes_list = []
all_ingredients = []
for i in range(n):
    recipe = take_recipe()
    for i in recipe['ingredients']:
        if i not in all_ingredients:
            all_ingredients.append(i)
    recipes_list.append(recipe)

data = {}

data['all_ingredients'] = all_ingredients
data['recipes_list'] = recipes_list

file = open(filename, 'wb')
pickle.dump(data, file)
file.close()
