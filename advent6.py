import string
import re

name = "advent6.txt"
handle = open(name)
numbers = handle.read()
numbers = [i for i in numbers]


checkstring = [i for i in range(14)]
counter = 14
for number in numbers:
    while counter > 0:
        checkstring.append(number)
        checkstring.remove(checkstring[0])
        counter = counter - 1
        break

numbers = numbers[14:]
index = 13
for number in numbers:
    index = index +  1
    y = len(set(checkstring))
    if y < 14:
        checkstring.append(number)
        checkstring = checkstring[1:]
    else:
        print(index)
        break
