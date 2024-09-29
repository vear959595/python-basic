import random

def roll():
    return random.randint(1,6)

counter = 0

for i in range(10000):
    counter += roll()

avg_roll = counter / 10000

print(f"average roll is {avg_roll}")
