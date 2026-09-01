class Animal:
    def __init__(self,name):
        self.name = name

    def makeSound(self):
        print("Animal Make Sound")

    def showDetails(self):
        print(f"Name: {self.name}")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name)
        self.breed=breed

    def makeSound(self):
        print("Bark")

    def showDetails(self):
        Animal.showDetails(self)
        print(f"Breed: {self.breed}")

class Cat(Animal):
    def __init__(self,name,color):
        Animal.__init__(self,name)
        self.color=color

    def makeSound(self):
        print("Meow")

    def showDetails(self):
        Animal.showDetails(self)
        print(f"Color: {self.color}")

o=Animal("Jhon")

o.showDetails()

o.makeSound()
