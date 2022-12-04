import re
import string

name = input("Enter file:")
if len(name) < 1:
    name = "advent4.txt"
handle = open(name)
numbers = handle.read()



numbers = numbers.split('\n')
#print(numbers)
counter = 0
for number in numbers:
    number = number.split(',')
    firstrange = number[0].split('-')
    secondrange = number[1].split('-')
    if int(firstrange[0]) <= int(secondrange[0]) and int(firstrange[1]) >= int(secondrange[1]):
        counter = counter + 1
       print(number)
        
    elif int(secondrange[0]) <= int(firstrange[0]) and int(secondrange[1]) >= int(firstrange[1]):
        counter = counter + 1
        print(number)



print(counter)
