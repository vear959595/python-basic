#Exercise 1
class Dog:
    species = "Canis familiars"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"


philo = Dog("Philo", 5, "brown")
print(f"{philo.name}`s coat is {philo.coat_color} ")

#Exercise 2

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def drive(self, miles):
        self.mileage += miles

blue = Car("blue", 20000)
red = Car("red", 30000)
new = Car("black", 0)


print(f"The {blue.color} has {blue.mileage} miles.")
print(f"The {red.color} has {red.mileage} miles.")