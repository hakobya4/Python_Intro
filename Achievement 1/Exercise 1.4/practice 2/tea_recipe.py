import pickle

tea_recipe = {
    "Ingredient Name": "Tea",
    "Ingredients": ["Tea leaves", "Water", "Sugar"],
    "Cooking Time": 5,
    "Difficulty": "Easy"
}

my_file = open('recipe_binary.bin', 'wb')
pickle.dump(tea_recipe, my_file)
my_file.close()

with open('recipe_binary.bin', 'rb') as my_file:
    tea_recipe = pickle.load(my_file)


print("Tea Recipe - ")
print("Name:  " + tea_recipe['Ingredient Name'])
print("Ingredients:  " + str(tea_recipe['Ingredients']))
print("Cooking Time: " + str(tea_recipe['Cooking Time']))
print("Difficulty: " + tea_recipe['Difficulty'])
