import json
f = open(r"Фирмы.txt", "r", encoding="UTF-8")
my_dict1 = {}
my_dict2 = {}
my_dict3 = {}
all_ = []
sr = 0
kol = 0
for line in f:
    surname = line.strip().split()
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
    k = (integers[0]) - (integers[1])
    if k > 0:
        my_dict1[surname[0]] = k
        sr += k
        kol += 1
    if k < 0:
        my_dict2[surname[0]] = k
my_dict3["average_profit"] = int(sr / kol)
all_.append(my_dict1)
all_.append(my_dict2)
all_.append(my_dict3)
print(all_)
with open("file.json", "w") as f:
    json.dump(all_, f)
f.close()