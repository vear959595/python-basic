import random

def unfair_coin_flip(probability_of_tails):
    if random.random() < probability_of_tails:
        return "tails"
    else:
        return "heads"

heads_counter = 0
tails_counter = 0

for trial in range(10000):
    if unfair_coin_flip(.7) == "heads":
        heads_counter += 1
    else:
        tails_counter += 1

ratio = heads_counter / tails_counter

print(f"The ratio of heads to tails is {ratio}")