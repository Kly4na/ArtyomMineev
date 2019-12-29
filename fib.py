"""Выводит заднное число Фибоначчи"""
import functools
import timeit

def fib_1(n_0: int) -> int:
    """Функция втупую подсчитывает значение числа Фибоначчи"""
    if n_0 in (1, 2):
        return 1
    return fib_1(n_0-1) + fib_1(n_0-2)

@functools.lru_cache()
def fib_2(n_0: int) -> int:
    """Функция подсчитывает значени числа Фибоначчи с мемоизацией"""
    if n_0 in (1, 2):
        return 1
    return fib_2(n_0-1) + fib_2(n_0-2)

N: int = int(input("Введите число" + '\n'))
print(fib_2(N))

T1: int = timeit.timeit("fib_1(N)", setup="from __main__ import fib_1, N", number=10000)
T2: int = timeit.timeit("fib_2(N)", setup="from __main__ import fib_2, N", number=10000)
print(T1, T2)
print(T1/T2)
