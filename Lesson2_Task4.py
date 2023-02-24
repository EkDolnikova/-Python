# Для списка реализовать обмен значений соседних элементов,
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = [int(i) for i in input("Введите числа через пробел: ").split()]
element = 0
for elem in range(int(len(my_list) / 2)):
    my_list[element], my_list[element + 1] = my_list[element + 1], my_list[
        element]
    element += 2

print(my_list)
