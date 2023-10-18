## Exercise 1.2

- name (str): Contains the name of the recipe
- cooking_time (int): Contains the cooking time in minutes
- ingredients (list): Contains a number of ingredients, each of the str data type

- The data structure that I decided to use for each recipe is dictionary.
This is because each recipe requires 3 key value pairs, putting the name, cooking time and ingredients in a list will without their keys will be confusing to read.
Additionally we would want to find a recpie by its name so having the name of each
recipe attached to a key Name will make it easier to find. Dictionaries are also mutable if we ever need to change a recipe and dictionaries can also hold multiple types of data which is important because we need to store a string (Name) and int(cooking time) and a list(ingredients).

- I decided to store each recipe inside of an outer structure all_recipes which is a list. This is because lists can be modified (mutable) and it stores items sequentially.