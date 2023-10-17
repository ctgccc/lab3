count=0
total_cost=0
average_cost =0

try:
    with open('Цветочки.txt', 'r', encoding='UTF-8') as file:
        print("Цветы дороже 5 руб:")
        for line in file:
            count+=1
            flower, price = line.split()
            if int(price) > 5:
                print(flower)
            total_cost += float(price)
        average_cost = total_cost / count  # len(flower)
        print("Средняя стоимость всех цветов:", average_cost)
    with open('Цветочки.txt', 'r', encoding='UTF-8') as files:
        print("Цветы с минимальной стоимостью:")
        for lines in files:
            flowers, prices = lines.split()
            if int(prices) < 5:
                print(flowers)
except IOError:
    print("Произошла ошибка ввода-вывода!")