set1 = set(map(int, input('Введите элементы 1-го списка: ').split(',')))
set2 = set(map(int, input('Введите элементы 2-го списка: ').split(',')))
set3 = set1 - set2
print('Результат: ', end='')
print(*set3, sep=', ')

