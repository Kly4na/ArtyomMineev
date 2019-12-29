import math
import numpy as np

iterations = 10

def my_ch(x):
    """Вычисление гиперболического косинуса при помощи частичного суммирования ряда Тейлора"""
    x_pow = 1
    multiplier = 1
    partial_sum = 1
    for n in range(1, iterations):
        x_pow *= x**2  # В цикле постепенно считаем степень
        multiplier *= 1/((2*n)*(2*n-1))  # факториал
        partial_sum += x_pow * multiplier
    
    return partial_sum

a = float(input("Введите аргумент чосинуса "))
print(my_ch(a))
print(1/2 * (np.exp(a) + np.exp(-a)))
