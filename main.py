per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = (int(input('Введите сумму: ')))
new_list = []
for value in per_cent.values():
    deposit = int((money * value) / 100)
    new_list.append(deposit)
print(f'Список новых значений {new_list}')
print(f'Максимальное значение {max(new_list)}')
