from random import random

def election(chance_win_to_A):
    if random() < chance_win_to_A:
        return "A"
    else:
        return "B"

for i in range(10000):

    votes_for_A = 0
    votes_for_B = 0
    election()