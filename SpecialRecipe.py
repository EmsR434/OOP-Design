from Recipe import Recipe
#subclass inheriting from recipe
class SpecialRecipe(Recipe):
    def __init__(self, name, ingredients, special_ingredient):
        super().__init__(name, ingredients) #inheritance: assessing parent's attributes
        self.special_ingredient = special_ingredient #public attribute
    
    def add_special_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        print(f"Added special ingredient (ingredient.name) to the recipe.")
    
    def print_special_recipe_name(self):
        print(f"Special Recipe: {self.name}")
