list1 = []
line = input("Введите данные построчно, последняя пустая строка будет свидетельствовать о завершении ввода: ")
while line != "":
    list1.append(line)
    line = input()

with open("F1.txt", "w") as f1:
    for item in list1:
        f1.write("%s\n" % item)

with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
    first_word = ""
    for line in f1:
        if not first_word:
            first_word = line.split()[0]
        if first_word not in line.split():
            f2.write(line)

with open("F2.txt", "r") as f2:
    first_line = f2.readline()
    consonants_count = sum(1 for letter in first_line if letter.lower() in 'бвгджзйклмнпрстфхцчшщъь')
    print("Количество согласных букв в первой строке файла F2:", consonants_count)