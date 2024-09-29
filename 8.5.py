while True:
    value = input("Type q or Q to exit: ")
    if value.lower() == "q":
        break


for i in range(1, 51):
    if i % 3 == 0:
        continue

    print(i)