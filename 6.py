weight = float(input('Введите значение веса в фунтах '))
height = float(input('Введите значение роста в дюймах '))
print('Ваш индекс массы тела составляет ', round(weight*703/height**2, 2))
