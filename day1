name = input("Enter file:")
if len(name) < 1:
    name = "advent2.txt"
handle = open(name)
numbers = handle.read()
list = numbers.split('\n')

biglist = []
workinglist = []
for number in list:
    if number != '':
        workinglist.append(number)
    else:
        x = 0
        for y in workinglist:
            x = x + int(y)
        biglist.append(x)
        workinglist = []

first = 0
second = 0
third = 0
for bignumber in biglist:
    if int(bignumber) > int(first):
        third = second
        second = first
        first = bignumber
    elif int(bignumber) > int(second):
        third = second
        second = bignumber
    elif int(bignumber) > int(third):
        third = bignumber
sum = first + second + third
print(sum)
