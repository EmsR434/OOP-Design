# new class inheriting from Chef
from Chef import Chef

class MasterChef(Chef):
    def __init__(self, name, expertise, signature_dish):
        super().__init__(name, cuisine=expertise) #inheritance: accessing parent's attributes
        self.expertise = expertise #public attribute
        self.signature_dish = signature_dish #public attribute
    
    def showcase_expertise(self):
        print(f"{self.name} specializes in {self.expertise} cuisine.") #public method
   
    def update_expertise(self, new_expertise):
        self.expertise = new_expertise
        print(f"Updated expertise to {new_expertise}.")
