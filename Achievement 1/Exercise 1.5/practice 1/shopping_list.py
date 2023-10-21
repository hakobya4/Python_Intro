class ShoppingList(object):
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
        else:
            print(str(item) + ' already in the list')

    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)

    def view_list(self):
        for i in self.shopping_list:
            print(i)


pet_store_list = ShoppingList("Pet Store Shopping List")

pet_store_list.add_item("dog")
pet_store_list.add_item("food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")


pet_store_list.remove_item("flea collars")

pet_store_list.add_item("frisbee")

pet_store_list.view_list()
