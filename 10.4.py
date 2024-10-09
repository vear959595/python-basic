class Animal:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years"

    def speak(self, sound):
        return f"{self.name} says {sound}"

    def eat(self):
        return f"{self.name} is eating right now. Don`t touch it"

    def walk(self):
        return f"{self.name} is walking"

    def sleep(self):
        return f"{self.name} is sleeping"

class Cow(Animal):
    def milk(self):
        return f"{self.name} give a milk"

    def speak(self, sound="moo moo"):
        return super().speak(sound)

class Sheep(Animal):
    def wool(self):
        return f"{self.name} give a wool"

    def speak(self, sound="Baaa Baaa"):
        return super().speak(sound)

class Pig(Animal):
    def swim(self):
        return f"{self.name} is swiming in mud"

    def speak(self, sound="Oink Oink"):
        return super().speak(sound)



#Create a cow

cow = Cow(1, "Zoika")

#Print some behaivor
print(cow.sleep())
print(cow.speak())

#create a pig

pig = Pig(2, "Svin")

print(pig)

#create a sheep

sheep = Sheep(5, "Ovechka")

print(sheep.speak())