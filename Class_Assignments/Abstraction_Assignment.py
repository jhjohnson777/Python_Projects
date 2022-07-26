
# import Abstract method from abc module
from abc import ABC, abstractmethod
class Base(ABC):
    def pBase(self): # Defines a base class method
        print("Base Class")

    @abstractmethod
    def pChild(self): # Abstract method to be defined in a child class
        pass # allows creation of a method without it being defined
    
class Child(Base): # Child class
    def pChild(self): # Defines method that was an abstraction in the parent class
        print("Child Class")

obj = Child() # creates object based on child class
obj.pBase() # calls base class method that is available to its child
obj.pChild() # prints child class method that was an abstraction in the parent class
