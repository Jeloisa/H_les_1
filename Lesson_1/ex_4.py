number = int(input('Введите целое положительное число: '))
a = 0
while number > 10 :
    b = number % 10
    number //= 10
    if a < b :
        a = b
print(a)