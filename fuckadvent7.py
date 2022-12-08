totalsize = 100000
name = "advent7.txt"
handle = open(name)
numbers = handle.read()

lines = numbers.split('\n')



current_dir = 0
directories = ['/']

for line in lines:
	if 'dir ' in line:
		line = line.split()
		if line[1] not in directories:
			directories.append(line[1])


orders = []
index = 0
for line in lines:
	if '$' in line:
		orders.append(index)
		orders.append(line)
	index += 1
commands = orders[1::2]
command_indices = orders[::2]


counter = 0
directory_inventories = []
for command in commands:
	if '$ ls' in command:
		to_add = []
		start = command_indices[counter] + 1
		try:
			end = command_indices[counter + 1]
		except:
			end = len(lines)
		directory = commands[counter - 1]
		directory = directory.split()
		directory = directory[2]
		to_add.append(directory)
		to_add.append(start)
		to_add.append(end)
		directory_inventories.append(to_add)
	counter += 1



index = 0
for line in lines:
	index += 1
	if '$' not in line and 'dir' not in line:
		line = line.split()
		lines[index - 1] = line[0]


#print(lines)
#print(directories)
#print(directory_inventories)
print(len(directories), len(directory_inventories))



directory = 0
list_values = []
master_list_values = []

for inventory in directory_inventories:
	directory = inventory[0]
	list_values = lines[inventory[1]:inventory[2]]
	master_list_values.append(list_values)


directory_order = [i[0] for i in directory_inventories]


directories_values = []
counter = 0
for each in reversed(master_list_values):
	index = 0
	directory_value = 0
	for number in each:
		if 'dir' not in number:
			directory_value = directory_value + int(number)
			index += 1
		elif 'dir' in number:
			number = number.split()
			dir_id = number[1]
			try:
				loc_of_dir_value = int(directories_values.index(dir_id)) - 1
				directory_value = directory_value + int(directories_values[loc_of_dir_value])
			except:
				continue
	directories_values.append(directory_value)
	which_directory = directory_order[master_list_values.index(each)]
	directories_values.append(which_directory)

diretories_values = list(set(directories_values))

answer = 0
for value in directories_values:
	try:
		if value < totalsize:
			answer = answer + value 
	except:
		continue
print(answer)


total_space = 70000000
update_space = 30000000
used_space = directories_values[-2]
available_space = total_space - used_space
needed_space = update_space - available_space

possibilities = []

for value in directories_values:
	try:
		if value > needed_space:
			possibilities.append(value)
		else:
			continue
	except:
		continue

possibilities.sort()
print(possibilities)
