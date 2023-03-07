per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите сумму, которую планируете положить под проценты:")
deposit = []
for value in per_cent:
    deposit.append(per_cent[value] * float(money) / 100)
max_deposit = max(deposit)
print(deposit)
print("Максимальная сумма, которую вы можете заработать — [%i]" % max_deposit)