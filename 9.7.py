import random

from capitals import capitals_dict

state, capital = random.choice(list(capitals_dict.items()))

while True:
    print(f"What is the capital of {state}")
    answer = input("Enter your answer or type \"Exit\": ")
    if answer.lower() == capital.lower():
        print("Correct")
        break
    elif answer.lower() == 'exit':
        print(capital)
        print('Goodbye')
        break