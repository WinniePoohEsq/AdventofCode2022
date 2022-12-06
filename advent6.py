name = "advent6.txt"
handle = open(name)
numbers = handle.read()
numbers = [i for i in numbers]


check_string = []
counter = 4
for number in numbers:
    while counter > 0:
        check_string.append(number)
        counter = counter - 1
        break

numbers = numbers[4:]
index = 3
for number in numbers:
    index = index + 1
    y = len(set(check_string))
    if y < 4:
        check_string.append(number)
        check_string = check_string[1:]
    else:
        print(index)
        break
