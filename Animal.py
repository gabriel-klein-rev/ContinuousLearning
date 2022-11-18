from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, type, name="", age=0):
        self.type = type
        self.name = name
        self.age = age

    def get_older(self):
        self.age += 1

    def get_age(self):
        return str(self.age)
    
    def set_age(self, age):
        self.age = age

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def get_older(self):
        self.age += 7

    def move(self):
        print(self.name + " runs.")



#cat = Animal("Cat", name="Garfield", age=12)
dog = Dog("Dog", "Fido", 12)

# print(cat.age)
# cat.get_older()
# print(cat.age)

print(dog.age)
dog.get_older()
print(dog.age)
dog.move()

