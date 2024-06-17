names_string = input("Enter a list of names: ")
names = names_string.split()


l = len(names)

import random
randint = random.randint(0,l-1)

print(names[randint], "is going to buy")

