from random import randint

def coin_flip():
    if randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

flip = 0

for i in range(10000):
    flip += 1
    if coin_flip() == "heads":
        while coin_flip() == "heads":
            flip += 1
        flip += 1
    else:
        flip += 1
        while coin_flip() == "tails":
            flip += 1
        flip += 1

avg = flip / 10000

print(f"average flips per trial is {avg}")