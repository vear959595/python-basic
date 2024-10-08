#Exercise 1

captains = {}

#Exercise 2

captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

#Exercise 3

if "Enterprise" not in captains:
    captains["Enterprise"] = "unknown"

if "Discovery" not in captains:
    captains["Discovery"] = "unknown"

#Exercise 4

for boat in captains:
    print(f"The {boat} is captained by {captains[boat]}")

#Exercise 5

del captains["Discovery"]
