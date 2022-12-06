name = "advent6.txt"
handle = open(name)
numbers = handle.read()
numbers = [i for i in numbers]


check_string = [i for i in range(14)]
counter = 14
for number in numbers:
    while counter > 0:
        check_string.append(number)
        check_string.remove(check_string[0])
        counter = counter - 1
        break

numbers = numbers[14:]
index = 13
for number in numbers:
    index = index + 1
    y = len(set(check_string))
    if y < 14:
        check_string.append(number)
        check_string = check_string[1:]
    else:
        print(index)
        break
