class Recipe(object):
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = ""

    def get_name(self):
        output = "Recipe: " + str(self.name)
        return output

    def set_name(self):
        return self.name

    def get_cooking_time(self):
        output = "Cooking Time:" + str(self.ingredients)
        return output

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    def add_ingredients(self, *ingredients):
        for i in ingredients:
            if i not in self.ingredients:
                self.ingredients.append(i)
                self.update_all_ingredients()

    def get_ingredients(self):
        output = "Ingredients: " + self.ingredients
        return output

    def calculate_difficulty(self, cooking_time, ingredients):
        if cooking_time < 10 and len(ingredients) < 4:
            self.difficulty = "easy"
        elif cooking_time < 10 and len(ingredients) >= 4:
            self.difficulty = "medium"
        elif cooking_time >= 10 and len(ingredients) < 4:
            self.difficulty = "intermediate"
        elif cooking_time >= 10 and len(ingredients) >= 4:
            self.difficulty = "hard"

    def get_difficulty(self):
        if not self.difficulty:
            self.calculate_difficulty(self.cooking_time, self.ingredients)
            output = "Difficulty: " + self.difficulty
            return output
        output = "Difficulty: " + self.difficulty
        return output

    def search_ingredient(self, ingredient):
        for i in self.ingredients:
            if i == ingredient:
                return True

    all_ingredients = []

    def update_all_ingredients(self):
        for i in self.ingredients:
            if not i in Recipe.all_ingredients:
                Recipe.all_ingredients.append(i)

    def __str__(self):
        output = (
            "Recipe Name: " + str(self.name) + "\n" +
            "Cooking Time: " + str(self.cooking_time) + "\n" +
            "Ingredients: " + str(self.ingredients) + "\n" +
            "Difficulty: " + str(self.difficulty) + "\n"
        )
        return output

    def recipe_search(data, search_term):
        for i in data:
            if i.search_ingredient(search_term):
                print(i)


recipes_list = []
tea = Recipe("Tea")
tea.add_ingredients("Tea leaves", "Sugar", "Water", "Salt")
tea.set_cooking_time(5)
tea.get_difficulty()
recipes_list.append(tea)

coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.set_cooking_time(5)
coffee.get_difficulty()
recipes_list.append(coffee)


cake = Recipe("Cake")
cake.add_ingredients(
    "Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"
)
cake.set_cooking_time(50)
cake.get_difficulty()
recipes_list.append(cake)


banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients(
    "Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
banana_smoothie.set_cooking_time(5)
banana_smoothie.get_difficulty()
recipes_list.append(banana_smoothie)

print("Recipe List: \n",)
for recipe in recipes_list:
    print(recipe)


print("Recipes with water: ")
Recipe.recipe_search(recipes_list, "Water")

print("Recipes with sugar: ")
Recipe.recipe_search(recipes_list, "Sugar")

print("Recipes with bananas: ")
Recipe.recipe_search(recipes_list, "Bananas")
