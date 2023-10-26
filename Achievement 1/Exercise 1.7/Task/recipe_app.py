from sqlalchemy import create_engine, Column

from sqlalchemy.orm import sessionmaker, declarative_base

from sqlalchemy.types import Integer, String

engine = create_engine('mysql://cf-python:password@localhost/my_database')

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'practice_recipes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # Shows a quick representation of the recipe
    def __repr__(self):
        return '<Recipe ID: ' + str(self.id) + '-' + self.name + ' Difficulty: ' + self.difficulty + ' >'

    # method that prints a well-formatted version of the recipe
    def __str__(self):
        return (
            '\n' + 'Recipe Id: ' + str(self.id) +
            '\nRecipe Name: ' + str(self.name) +
            '\nCooking Time: ' + str(self.cooking_time) +
            '\nIngredients: ' + str(self.ingredients) +
            '\nDifficulty: ' + str(self.difficulty)
        )

    # calculate the difficulty of a recipe based on the number of ingredients and cooking time
    def calculate_difficulty(self):
        ingredients = self.ingredients.split(", ")
        if self.cooking_time < 10 and len(ingredients) < 4:
            self.difficulty = "Easy"
        if self.cooking_time < 10 and len(ingredients) >= 4:
            self.difficulty = "Medium"
        if self.cooking_time >= 10 and len(ingredients) < 4:
            self.difficulty = "Intermediate"
        if self.cooking_time >= 10 and len(ingredients) >= 4:
            self.difficulty = "Hard"

    # retrieves the ingredients string inside your Recipe object as a list
    def return_ingredients_as_list(self):
        if self.ingredients == '':
            return []
        else:
            return Recipe.ingredients.split(', ')

    Base.metadata.create_all(engine)

    def create_recipe():
        name = str(input('Enter recipe name (max: 50 chars): '))

        while (not name or len(name) > 50 or not name.strip().isalnum()):
            if not name:
                print('Error: Input is empty')
                name = str(input('Enter recipe name (max: 50 chars): '))
            elif len(name) > 50:
                print('Error: Input is larger than 50 characters')
                name = str(input('Enter recipe name (max: 50 chars): '))
            elif not name.strip().isalnum():
                print('Error: Input should not include special characters')
                name = str(input('Enter recipe name (max: 50 chars): '))
        print('Success! Next input cooking time')

        cooking_time = input('Cooking Time: ')

        while (not cooking_time.strip().isnumeric() or not cooking_time):
            if not cooking_time:
                print('Error: Input is empty')
                cooking_time = input('Cooking Time: ')
            elif not cooking_time.strip().isnumeric():
                print('Error: Input should be one number')
                cooking_time = input('Cooking Time: ')
        cooking_time = int(cooking_time)
        print('Success! Next input number of ingredients in the recipe: ')

        n = input('Number of ingredients: ')
        while (not n.strip().isnumeric() or not n):
            if not n.strip().isnumeric():
                print('Error: Input should be a number')
                n = input('Number of ingredients: ')
            elif not n:
                print('Error: Input is empty')
                n = input('Number of ingredients: ')
        print('Success! Next input ingredients one at a time: ')

        ingredients = []
        for i in range(int(n)):
            ingredient = str(input('Enter ingredient (max: 50 chars): '))
            while (not ingredient or not ingredient.strip().isalpha() or len(ingredient) > 50):
                if not ingredient:
                    print('Error: Input is empty')
                    ingredient = str(
                        input('Enter ingredient (max: 50 chars): '))
                elif len(name) > 50:
                    print('Error: Input is larger than 50 characters')
                    ingredient = str(
                        input('Enter ingredient (max: 50 chars): '))
                elif not ingredient.strip().isalpha():
                    print(
                        'Error: Input should not include special characters or numbers')
                    ingredient = str(
                        input('Enter ingredient (max: 50 chars): '))

            if len(ingredient) <= 50:
                if ingredient not in ingredients:
                    ingredients.append(ingredient)
                    print('Ingredient ' + str(i+1) + ' added, ' +
                          str(int(n)-(i+1)) + ' to go')

            ingredients_string = ', '.join(ingredients)

        print('Recipe Created!')

        recipe_entry = Recipe(
            name=name,
            cooking_time=int(cooking_time),
            ingredients=ingredients_string,
        )
        recipe_entry.calculate_difficulty()
        session.add(recipe_entry)
        session.commit()

    def view_all_recipes():
        recipes = session.query(Recipe).all()
        if not recipes:
            print('No recipes')
            return None
        for recipe in recipes:
            print(recipe)
        back = input('Press 1 to go back to main menu: ')
        while back != '1':
            back = input('Press 1 to go back to main menu: ')

        if back == '1':
            return None

    def search_by_ingredients():
        list = session.query(Recipe).count()
        if list == 0:
            print('There are no recipes in the database')
            return None
        all_ingredients = []
        results = session.query(Recipe.ingredients).all()
        for i in results:
            ingredients = i[0]
            ingredient = ingredients.split(', ')
            for i in ingredient:
                if i not in all_ingredients:
                    all_ingredients.append(i)

        print('All ingredients: ')
        for index, ingredient in enumerate(all_ingredients):
            print(str(index) + '. ' + ingredient)

        n = input('Enter number of ingredient(s) (n1 n2 n3): ')

        while (not n or not n.replace(" ", "").isdigit() or
               # making sure that all the values that the user types do not pass the number of ingredients displayed.
               max(int(i) for i in n.split()) > len(all_ingredients)-1):
            if not n:
                print('Error: Missing Input')
                n = input('Enter number of ingredient(s) (n1 n2 n3): ')
            elif not n.replace(" ", "").isdigit():
                print('Error: Input must be a number')
                n = input('Enter number of ingredient(s) (n1 n2 n3): ')
            elif max(int(i) for i in n.split()) > len(all_ingredients)-1:
                print('Error: Invalid Input')
                n = input('Enter number of ingredient(s) (n1 n2 n3): ')

        # adding inputs of the user into a list of ints
        ingredients_number = [int(i) for i in n.split()]
        # going through the user inputs and finding their respective ingredients -put into list
        ingredients_searched = [all_ingredients[i] for i in ingredients_number]
        conditions = []

        for i in ingredients_searched:
            # searching each ingredient from a list available in recepies and appending it as conditions
            conditions.append(Recipe.ingredients.like('%' + i + '%'))

        # filtering all recepies that have all the conditions
        recipes = session.query(Recipe).filter(*conditions).all()

        if not recipes:
            print('No recipes found with this combination')
            return None
        print('Recipes: ')
        recipes = session.query(Recipe).filter(*conditions).all()
        for recipe in recipes:
            print(recipe)
            return None

    def edit_recipe():
        recipes = session.query(Recipe).all()
        if not recipes:
            print('No recipes')
            return None
        results = []
        for recipe in recipes:
            results.append((recipe.id, recipe.name))

        for i in results:
            recipes_search = (session.query(
                Recipe).filter(Recipe.id == i[0]).all())
            for recipe in recipes_search:
                print(recipe)

        recipe_id = input('Enter Id of the recipe: ')

        id_of_recipes = []
        for recipe in session.query(Recipe.id).all():
            id_of_recipes.append(recipe.id)
        while (
            not recipe_id
            or not recipe_id.isnumeric()
            or int(recipe_id) not in id_of_recipes
        ):
            if not recipe_id:
                print('Error: Missing input')
                recipe_id = input('Enter Id of the recipe: ')
            elif not recipe_id.isnumeric():
                print('Error: The input should be a number ')
                recipe_id = input('Enter Id of the recipe: ')
            elif int(recipe_id) not in id_of_recipes:
                print('Error: The recipe is not in the list')
                return None

        recipe_to_edit = session.query(Recipe).get(int(recipe_id))
        print('Choose the part of the recipe to update:')
        print('1. Name: ', recipe_to_edit.name)
        print('2. Cooking time: ', recipe_to_edit.cooking_time)
        print('3. Ingredients: ', recipe_to_edit.ingredients)

        n = input('Choose the part of the recipe to update: ')

        while (
            not n or not n.strip().isnumeric() or not 0 < int(n) <= 3
        ):
            if not n:
                print('Error: Missing Input')
                n = input('Choose the part of the recipe to update: ')
            elif not n.strip().isnumeric():
                print('Error: Input must be a number')
                n = input('Choose the part of the recipe to update: ')
            elif not 0 < int(n) <= 3:
                print('Error: Invalid Input')
                n = input('Choose the part of the recipe to update: ')

        if int(n) == 1:
            new_name = input('Enter new name (max chars: 50): ')

            while (
                not new_name
                or not new_name.replace(" ", "").isalnum()
                or len(new_name) > 50
            ):
                if not new_name:
                    print('Error: Missing Input')
                    new_name = input('Enter new name: ')
                elif not new_name.replace(" ", "").isalnum():
                    print('Error: Input must only contain no special characters')
                    new_name = input('Enter new name: ')
                elif len(new_name) > 50:
                    print('Error: Max character must be 50')
                    new_name = input('Enter new name: ')
            print('Success!')
            recipe_to_edit.name = new_name
            session.add(recipe_to_edit)
            session.commit()
            return None

        elif int(n) == 2:
            new_time = input('New Cooking Time:')
            while (not new_time.strip().isnumeric() or not new_time):
                if not new_time:
                    print('Error: Input is empty')
                    new_time = input('New Cooking Time: ')
                elif not new_time.strip().isnumeric():
                    print('Error: Input should be a number')
                    new_time = input('Cooking Time: ')

            new_recipe = Recipe(
                name=recipe_to_edit.name,
                cooking_time=int(new_time),
                ingredients=recipe_to_edit.ingredients,
            )
            new_recipe.calculate_difficulty()
            session.query(Recipe).filter(Recipe.id == recipe.id).update(
                {
                    Recipe.cooking_time: int(new_time),
                    Recipe.difficulty: new_recipe.difficulty,
                }
            )
            session.commit()
            print("Updated!")
            return None

        elif int(n) == 3:
            num = input('New number of ingredients: ')
            while (not num.strip().isnumeric() or not num):
                if not num.strip().isnumeric():
                    print('Error: Input should be a number')
                    num = input('New number of ingredients: ')
                elif not n:
                    print('Error: Input is empty')
                    num = input('New number  of ingredients: ')
            print('Next input the new ingredients one at a time: ')

            new_ingredients = []
            for i in range(int(num)):
                new_ingredient = input('Enter ingredient (max: 50 chars): ')
                while (not new_ingredient or not new_ingredient.strip().isalpha() or len(new_ingredient) > 50):
                    if not new_ingredient:
                        print('Error: Input is empty')
                        new_ingredient = input(
                            'Enter ingredient (max: 50 chars): ')
                    elif len(new_ingredient) > 50:
                        print('Error: Input is larger than 50 characters')
                        new_ingredient = input(
                            'Enter ingredient (max: 50 chars): ')
                    elif not new_ingredient.replace(" ", "").isalpha():
                        print(
                            'Error: Input should not include special characters or numbers')
                        new_ingredient = input(
                            'Enter ingredient (max: 50 chars): ')

                if len(new_ingredient) <= 50:
                    if new_ingredient not in new_ingredients:
                        new_ingredients.append(new_ingredient)
                        print('Ingredient ' + str(i+1) + ' added, ' +
                              str(int(num)-(i+1)) + ' to go')

            new_ingredients = ', '.join(new_ingredients)

            new_recipe = Recipe(
                name=recipe_to_edit.name,
                cooking_time=recipe_to_edit.cooking_time,
                ingredients=new_ingredients,
            )
            new_recipe.calculate_difficulty()
            session.query(Recipe).filter(Recipe.id == recipe.id).update(
                {
                    Recipe.ingredients: new_ingredients,
                    Recipe.difficulty: new_recipe.difficulty,
                }
            )
            session.commit()
            print("Updated!")
            return None

    def delete_recipe():
        recipes = session.query(Recipe).all()
        if not recipes:
            print('No recipes')
            return None
        results = []
        for recipe in recipes:
            results.append((recipe.id, recipe.name))

        for recipe in results:
            recipe_id = recipe[0]
            all_recipes = (session.query(Recipe).filter(
                Recipe.id == recipe_id).all())
            for recipe in all_recipes:
                print(recipe)

        del_id = input('Id of recipe to delete: ')

        while (
            not del_id
            or not del_id.isnumeric()
        ):
            if not del_id.strip():
                print('Error: Missing Input')
                del_id = input('Id of recipe to delete: ')
            elif not del_id.isnumeric():
                print('Error: Input must be a number')
                del_id = input('Id of recipe to delete: ')
        if 1 > int(del_id) > len(recipes):
            print('Error: Invalid Input')
            return None

        delete_message = input('Are you sure? Enter yes or no: ').lower()
        while delete_message not in ['yes', 'no']:
            print('Error: Invalid Input')
            delete_message = input('Are you sure? Enter yes or no: ').lower()

        if delete_message == 'yes':
            recipe_del = (session.query(Recipe).filter(
                Recipe.id == del_id).one())
            session.delete(recipe_del)
            session.commit()
            print('Deleted!')
            return None

        elif delete_message == 'no':
            return None


def main_menu():
    input_value = None

    while input != 'quit':
        print('-' * 25)
        print('Main menu')
        print('-' * 25)
        print('Choices')
        print('1. Create a new recipe')
        print('2. View all recipes')
        print('3. Search for a recipe by ingredients')
        print('4. Edit a recipe')
        print('5. Delete a recipe')
        print('Type "quit" to exit')
        input_value = input('Your choice: ')

        if input_value == '1':
            Recipe.create_recipe()
        elif input_value == '2':
            Recipe.view_all_recipes()
        elif input_value == '3':
            Recipe.search_by_ingredients()
        elif input_value == '4':
            Recipe.edit_recipe()
        elif input_value == '5':
            Recipe.delete_recipe()
        elif input_value.lower() == 'quit':
            session.close()
            engine.dispose()
            break
        else:
            print('Error: Wrong Input')
            continue


main_menu()
