import pickle


def display_recipe(recipe):
    print("Recipe Name: ", recipe["name"])
    print("Cooking Time: ", recipe["cooking_time"])
    print("Ingredients: ")
    for i in recipe["ingredients"]:
        print(i)
    print("Difficulty: ", recipe["difficulty"])


def search_ingredient(data):
    ingredients = list(enumerate(data["all_ingredients"]))

    for i in ingredients:
        print(i[0], i[1])

    try:
        n = int(input("Enter the ingredient number: "))
        ingredient_searched = ingredients[n][1]
    except:
        print("Incorrect Input")
    else:
        for i in data["recipes_list"]:
            if ingredient_searched in i["ingredients"]:
                print(i)


filename = input("Enter the name of the file that contains your recipe data: ")
try:
    file = open(filename, "rb")
    data = pickle.load(file)
except FileNotFoundError:
    print("File doesn't exist - exiting")
except:
    print("An unexpected error occurred.")
else:
    search_ingredient(data)
    file.close()
