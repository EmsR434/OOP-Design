class Recipe:
    def __init__(self, name, ingredients):
        self.name = name #public attribute
        self.ingredients = ingredients # public attribute, list of ingredient objects
   
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        print(f"Added (ingredient.name) to the recipe.")

    def print_recipe_name(self):
        print(f"Recipe: {self.name}")
