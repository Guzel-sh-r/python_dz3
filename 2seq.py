spisok = input('Введите элементы списка через запятую, точку с запятой или слэш: ')
separator = ','
if spisok.find(';') >= 0:
    separator = ';'
elif spisok.find('/') >= 0:
    separator = '/'
spisok = list(spisok.split(separator))
answer = []
for i in spisok:
    if spisok.count(i) == 1:
        answer.append(i)
print('Результат: ', end='')
print(*answer, sep=', ')
