
import re
import string

name = input("Enter file:")
if len(name) < 1:
    name = "advent3.txt"
handle = open(name)
numbers = handle.read()
allbags = numbers.split('\n')

def divide_list(l, n):
	for i in range(0, len(l), n):
		yield l[i:i + n]
		
listofgroups = list(divide_list(allbags, 3))

badges = []
for group in listofgroups:
	group1 = group[0]
	group2 = group[1]
	group3 = group[2]
	for badge in group1:
		x = re.search(badge, group2)
		if x:
			x = re.search(badge, group3)
			if x:
				badges.append(x.group())
				break

alphabet = (string.ascii_letters)
totalpoints = 0
for badge in badges:
    value = 0
    value = int(alphabet.index(badge)) + 1
    totalpoints = totalpoints + value
print(totalpoints)
