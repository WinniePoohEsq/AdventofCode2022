columns = open("advent5_fullinput.txt")
columns = columns.read()
columns = columns.split("\n\n")
initial = columns[0]
directions = columns[1]


biglist = []
workinglist = []

initial = initial.split('\n')
for i in initial:
    i = i.replace('[', '').replace(']', '').replace('  ', ' ').replace('\n', '')
    workinglist.append(i)

workinglist = workinglist[:-1]

for item in workinglist:
    item = item[::2]
    biglist.append(item)

workinglistoflists = [i for i in range(9)]

for item in biglist:
    counter = 0
    for i in item:
        column = workinglistoflists[counter]
        column = str(column) + i
        workinglistoflists[counter] = column
        counter += 1

finalist = []
for i in workinglistoflists:
    i = i[1:]
    i = i[::-1]
    i = i.strip(' ')
    finalist.append(i)

columns = finalist
#columns = ["RNFVLJSM", "PNDZFJWH", "WRCDG", "NBS", "MZWPCBFN", "PRMW", "RTNGLSW", "QTHFNBV", "LMHZNF"]
#columns = ["zn", "mcd", "p"]

directions = directions.split("\n")
for direction in directions:
    direction = direction.split()
    tomove_count = int(direction[1])
    fromcolumnid = int(direction[3]) - 1
    fromcolumn = columns[fromcolumnid]
    tocolumnid = int(direction[5]) - 1
    tocolumn = columns[tocolumnid]
    if tomove_count > int(len(fromcolumn)):
        tomove_count = int(len(fromcolumn))
    tomove_letters = fromcolumn[-tomove_count:]
    for letter in reversed(tomove_letters):
    #for letter in (tomove_letters):
        tocolumn = tocolumn + letter
    fromcolumn = fromcolumn[:-tomove_count]
    columns[fromcolumnid] = fromcolumn
    columns[tocolumnid] = tocolumn

answer = ""
for column in columns:
    if len(column) > 0:
        answer = answer + column[-1]
print(answer)
