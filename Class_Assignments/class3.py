

# Parent Class
class Birds:
    height = "unknown"
    color = "unknown"
    wingspan = 0
    
    def intro(self): # parent method
        msg = "Look at all the birds."
        return msg

# Child class1
class Finch(Birds):
    height = "small"
    color = "yellow"
    wingspan = 5
    sings = True # new attribute
    speed = 3 # new attribute

    def intro(self): # same method with diff output for child1
        msg = "This is a finch."
        return msg

# Child class2
class Falcon(Birds):
    height = "medium"
    color = "gray"
    wingspan = 40
    top_speed = 10 # new attribute
    diet = "carnivore" # new attribute

    def intro(self): # same method with diff output for child2
        msg = "This is a falcon."
        return msg

# call these functions when document opens
if __name__ == "__main__":
    birds = Birds()
    print(birds.intro())

    finch = Finch()
    print(finch.intro())

    falcon = Falcon()
    print(falcon.intro())
