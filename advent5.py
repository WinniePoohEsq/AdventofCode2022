import re
import string

name = input("Enter file:")
if len(name) < 1:
    name = "advent5.txt"
handle = open(name)
directions = handle.read()

columns = ["RNFVLJSM", "PNDZFJWH", "WRCDG", "NBS", "MZWPCBFN", "PRMW", "RTNGLSW", "QTHFNBV", "LMHZNF"]
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
    #one line change for second part
    #for letter in reversed(tomove_letters):
    for letter in (tomove_letters):
        tocolumn = tocolumn + letter
    fromcolumn = fromcolumn[:-tomove_count]
    columns[fromcolumnid] = fromcolumn
    columns[tocolumnid] = tocolumn

answer = ""
for column in columns:
    if len(column) > 0:
        answer = answer + column[-1]
print(answer)
