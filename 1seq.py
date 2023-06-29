num = int(input('Введите количество элементов: '))
spisok = []
for i in range(num):
    element = int(input(f'Введите {i + 1} элемент: '))
    spisok.append(element)
print('Вывод:', sorted(spisok))

