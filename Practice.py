count = int(input("Введите количество билетов:"))
S = 0
for price in range (1, count + 1):
    age = int(input("Введите возраст посетителей:"))
    if 0 <= age <= 18:
        price = 0
    elif 18 <= age <= 25:
        price = 990
    elif 25 <= age <= 99:
        price = 1390
    else:
        print("Введите корректный возраст!")
if count > 3:
    S = (S + ((price * count)*0.9))
    print("Общая стоимость билетов:",S)
else:
    S = (S + (price * count))
    print("Общая стоимость билетов:",S)
