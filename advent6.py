import string
import re

name = "advent6.txt"
handle = open(name)
numbers = handle.read()
numbers = [i for i in numbers]

letters_value = [i for i in range(26)]
alphabet = (string.ascii_lowercase)
alphabet = [i for i in alphabet]

for value in reversed(letters_value):
    location = value
    alphabet.insert(location, value)

working_list = []
for number in numbers:
    location = alphabet.index(number)
    value = alphabet[location - 1]
    working_list.append(value)

#change range, counter for second part
checkstring = [i for i in range(14)]
counter = 14
for number in working_list:
    while counter > 0:
        checkstring.append(number)
        checkstring.remove(checkstring[0])
        counter = counter - 1
        break

#change range, index, y for second part
working_list = working_list[14:]
index = 13
for number in working_list:
    index = index +  1
    y = len(set(checkstring))
    if y < 14:
        checkstring.append(number)
        checkstring = checkstring[1:]
    else:
        print(index)
        break
