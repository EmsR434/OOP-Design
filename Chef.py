#class with composition
class Chef:
    def __init__(self, name, cuisine):
        self.name = name #public attribute
        self.cuisine = cuisine #public attribute
        self.recipe_book = {} #composition: dictionary to store recipes

    def add_recipe(self, recipe_name, recipe):
        self.recipe_book[recipe_name] = recipe #public method

    def print_chef_name(self):
        print(f"Chef: {self.name}")

    def update_recipe(self, recipe_name, new_recipe):
        self.recipe_book[recipe_name] = new_recipe
        print(f"Updated {recipe_name} in the recipe book.")
      
