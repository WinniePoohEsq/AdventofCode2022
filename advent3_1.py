
import re
import string

name = input("Enter file:")
if len(name) < 1:
    name = "advent3.txt"
handle = open(name)
numbers = handle.read()
list = numbers.split('\n')
similaritems = []

for bigsack in list:
    ruckone = bigsack[0:int(int(len(bigsack))/2)]
    rucktwo = bigsack[int(int(len(bigsack))/2):]

#   res = [item for item in rucktwo if item in ruckone]
#   similaritems.append(res)

#   for item1 in ruckone:
#        for item2 in rucktwo:
#            if item1 == item2:
#                similaritems.append(item2)
#                break

    for item1 in ruckone:
        x = re.search(item1, rucktwo)
        if x:
            similaritems.append(x.group())
            break
    

alphabet = (string.ascii_letters)
totalpoints = 0
for item in similaritems:
    value = 0
    value = int(alphabet.index(item)) + 1
    totalpoints = totalpoints + value
print(totalpoints)
