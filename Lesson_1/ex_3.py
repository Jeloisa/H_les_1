number = int(input('Введите одно натуральное число: '))
if 0 < number < 10:
    print( (number + number*10 + number*100) + (number + number*10) + number )
else:
    print('Вы ввели неверное число.\nКонец программы.')