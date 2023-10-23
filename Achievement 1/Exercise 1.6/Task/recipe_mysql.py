import mysql.connector

conn = mysql.connector.connect(
    host='localhost', user='cf-python', passwd='password')

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
     item_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
    )''')


def main_menu(conn, cursor):
    choice = ""
    while (choice != "5"):
        print("Pick a choice:")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Quit")
        choice = input("Your choice: ")

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)


def create_recipe(conn, cursor):
    name = str(input("Enter recipe name: "))
    cooking_time = int(input("Cooking Time: "))
    ingredient = input("Ingredients: ")
    ingredients = []
    ingredients.append(ingredient)
    difficulty = calculate_difficulty(cooking_time, ingredients)
    ingredients_join = ", ".join(ingredients)
    sql = 'INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
    val = (name, ingredients_join, cooking_time, difficulty)

    cursor.execute(sql, val)
    conn.commit()
    print("Recipe Created!")


def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    elif cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "Hard"
    return difficulty


def search_recipe(conn, cursor):
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    all_ingredients = []
    for i in results:
        for j in i:
            recipe_split = j.split(", ")
            all_ingredients.extend(recipe_split)

    all_ingredients = list(dict.fromkeys(all_ingredients))

    enumerate_all_ingredients = list(enumerate(all_ingredients))

    print("All ingredients list:")

    for index, tup in enumerate(enumerate_all_ingredients):
        print(str(tup[0]+1) + ". " + tup[1])

    try:
        n = input("Number of the ingredient: ")
        n_ingredient = int(n) - 1
        ingredient = enumerate_all_ingredients[n_ingredient][1]
    except:
        print("Wrong input")
    else:
        print("Recipes: ")
        cursor.execute(
            "SELECT * FROM Recipes WHERE ingredients LIKE %s", ('%' + ingredient + '%', ))

        results = cursor.fetchall()
        for i in results:
            print("id: ", i[0])
            print("Name: ", i[1])
            print("Ingredients: ", i[2])
            print("Cooking Time: ", i[3])
            print("Difficulty: ", i[4])


def update_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    for i in results:
        print("id: ", i[0])
        print("Name: ", i[1])
        print("Ingredients: ", i[2])
        print("Cooking Time: ", i[3])
        print("Difficulty: ", i[4])
    recipe_id = int((input("Enter Recipe Id: ")))
    update_column = str(input("Column to update: "))
    value = (input("New Value: "))

    if update_column == "Name":
        cursor.execute(
            "UPDATE Recipes SET name = %s WHERE  item_id = %s", (value, recipe_id))
        print("Updated")

    elif update_column == "Cooking Time":
        cursor.execute(
            "UPDATE Recipes SET cooking_time = %s WHERE item_id = %s", (value, recipe_id))
        cursor.execute(
            "SELECT * FROM Recipes WHERE item_id = %s", (recipe_id,))
        result = cursor.fetchall()

        ingredients = tuple(result[0][2].split(','))
        cooking_time = result[0][3]

        difficulty = calculate_difficulty(cooking_time, ingredients)
        cursor.execute(
            "UPDATE Recipes SET difficulty = %s WHERE item_id = %s", (difficulty, recipe_id))
        print("Updated")

    elif update_column == "Ingredients":
        cursor.execute(
            "UPDATE Recipes SET ingredients = %s WHERE item_id = %s", (value, recipe_id))
        cursor.execute(
            "SELECT * FROM Recipes WHERE item_id = %s", (recipe_id,))
        result = cursor.fetchall()

        ingredients = tuple(result[0][2].split(','))
        cooking_time = result[0][3]
        difficulty = result[0][4]

        updated_difficulty = calculate_difficulty(cooking_time, ingredients)
        cursor.execute(
            "UPDATE Recipes SET difficulty = %s WHERE item_id = %s", (updated_difficulty, recipe_id))
        print("Updated")

    conn.commit()


def delete_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    for i in results:
        print("id: ", i[0])
        print("Name: ", i[1])
        print("Ingredients: ", i[2])
        print("Cooking Time: ", i[3])
        print("Difficulty: ", i[4])
    delete_id = (input("Enter Id: "))
    cursor.execute("DELETE FROM Recipes WHERE item_id= (%s)", (delete_id, ))

    conn.commit()
    print("Deleted")


main_menu(conn, cursor)
