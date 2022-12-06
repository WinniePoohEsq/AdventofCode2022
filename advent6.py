name = "advent6.txt"
x = int(input("Messenge Length:"))
handle = open(name)
numbers = handle.read()
numbers = [i for i in numbers]


check_string = []
counter = x
for number in numbers:
    while counter > 0:
        check_string.append(number)
        counter = counter - 1

numbers = numbers[x:]
index = x
for number in numbers:
    y = len(set(check_string))
    if y < x:
        check_string.append(number)
        index = index + 1
        check_string = check_string[1:]
    else:
        print(index)
        break
