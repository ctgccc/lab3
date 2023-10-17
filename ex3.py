f = open(r"Предметы.txt", "r", encoding="UTF-8")
my_dict = {}
for line in f:
    surname = line.strip().split()
    surname1 = surname[0][:-1]
    length = len(line)
    integers = []
    i = 0
    while i < length:
        line_int = ''
        while i < length and '0' <= line[i] <= '9':
            line_int += line[i]
            i += 1
        i += 1
        if line_int != '':
            integers.append(int(line_int))
    my_dict[surname1] = sum(integers)
print(my_dict)
f.close()