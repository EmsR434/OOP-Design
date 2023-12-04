#class demonstrating composition
class Ingredient:
    def __init__(self, name, quantity):
        self.name = name #public attribute
        self.quantity = quantity #public attribute
    def use(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            print(f"Used {amount} units of {self.name}.")
        else:
            print(f"Not enough {self.name} available.")
