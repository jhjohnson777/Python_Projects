

# Created class
class Lizards:
    def __init__(self):
        self._length = 20 # Single underscore denotes a protected attribute
        self.__endangered = True # Double underscore denotes a private attribute

    def getEndangered(self): # Function is required to access or change a private attribute outside its defined class 
        print(self.__endangered)

Iguana = Lizards() # Create obj Iguana with Lizard class
print(Iguana._length) # Prints Iguana with predetermined length given in class creation
Iguana.getEndangered() # Prints Iguana with predetermined and more difficult to change private attribute given in class creation
