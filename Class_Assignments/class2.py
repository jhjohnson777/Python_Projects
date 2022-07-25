

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

ford = Car("mustang", "red")
chevrolet = Car("corvette", "blue")
honda = Car("nsx", "white")

print("John drives a {} {}.".format(ford.color,ford.model))
print(ford)
print(Car)
