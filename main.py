bileti = int(input('Введите число билетов которые хотите купить: '))
spisok = []
for i in range(1,bileti+1):
    f = int(input(f'Введите возвраст {i} посетителя: '))
    if f < 18:
        spisok.append(0)
    elif 18 <= f < 25:
        spisok.append(990)
    elif  f >= 25:
        spisok.append(1390)
if len(spisok)>3:
    rasx = sum(spisok)- sum(spisok)/100*10
    print(int(rasx), 'Сумма к оплате с учетом скидки 10%')
else:
    print(sum(spisok),' Ваша сумма к оплате')