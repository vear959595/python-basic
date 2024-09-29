import random
def coin_flip():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

heads_counter = 0
tails_counter = 0

for i in range(10000):
    if coin_flip() == "heads":
        heads_counter += 1
    else:
        tails_counter += 1

print(heads_counter)
print(tails_counter)