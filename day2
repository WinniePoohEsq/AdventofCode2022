name = input("Enter file:")
if len(name) < 1:
    name = "rps.txt"
handle = open(name)
numbers = handle.read()
list = numbers.split('\n')
#print(list)
scoretotal = 0
for x in list:
    if x == 'A Y':
        scoretotal = scoretotal + 4
    if x == 'A X':
        scoretotal = scoretotal + 3
    if x == 'A Z':
        scoretotal = scoretotal + 8
    if x == 'B Y':
        scoretotal = scoretotal + 5
    if x == 'B X':
        scoretotal = scoretotal + 1
    if x == 'B Z':
        scoretotal = scoretotal + 9
    if x == 'C Y':
        scoretotal = scoretotal + 6
    if x == 'C X':
        scoretotal = scoretotal + 2
    if x == 'C Z':
        scoretotal = scoretotal + 7
print(scoretotal)           
