ticket = int(input('укажите количество билетов '))
numbers_ages = []
for i in range(0, ticket):
    input_value = int(input(f'Введите возраст участника №{i + 1} '))
    numbers_ages.append(input_value)

    def price(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390

total_price = sum(map(price, numbers_ages))
discount_price = int(total_price * 0.9)
if ticket > 3:
    print('Стоимость всех билетов со скидкой: ', discount_price, "руб.")
else:
    print('Стоимость всех билетов: ', total_price, "руб.")