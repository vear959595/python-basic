#Exercise 1
from ast import Index

while True:
    try:
        int(input())
        break
    except ValueError:
        print("Try again!")

#Exercise 2
try:
    n = int(input("Enter a number: "))
except ValueError:
    print("You must type a number")
find_string = input("Enter a string: ")


try:
    print(find_string[n])
except IndexError:
    print("Number must be in a range of string")
except NameError:
    print("N is not defined")