from Ingredient import Ingredient
from Recipe import Recipe
from SpecialRecipe import SpecialRecipe
from Chef import Chef
from MasterChef import MasterChef

def start_cooking_game():
    potato = Ingredient("Potato", 5) 
    onion = Ingredient("Onion", 3)
    tomato = Ingredient("Tomato", 2)

    regular_recipe = Recipe("Regular Soup", [potato, onion, tomato])
    special_recipe= SpecialRecipe("Special Soup", [potato, onion, tomato], "Magic Spice")

    chef = Chef("Gordon Ramsay", "International")
    chef.add_recipe("Regular", regular_recipe)
    chef.add_recipe("Special", special_recipe)

    master_chef = MasterChef("marco Pierre White", "French", "Coq au Vin")
    master_chef.showcase_expertise()
    master_chef.update_expertise("Italian")
    master_chef.add_recipe("Pasta Dish", special_recipe)

    print ("Welcome to the Cooking Game!")
    while True:
        print("\nChoose an action:")
        print("1. Cook a regular recipe")
        print("2. Cook a special recipe")
        print("3. Check expertise of Master Chef")
        print("4. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            chef.cook_recipe("Regular")
        elif choice == "2":
            chef.cook.recipe("Special")
        elif choice == "3":
            master_chef.showcase_expertise()
        elif choice == "4":
            print("Exiting the Cooking Game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

start_cooking_game
