# Задание 3.
# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.

a = input('Введите целое положительное число:')
b = a * 2
c = a * 3
d = int(a) + int(b) + int(c)
print(d)
