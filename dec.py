def repeat(n):
    def decorator(func):
        def fake_func(x):
            for i in range(n):
                x=func(x)
            return x
        return fake_func
    return decorator

@repeat(2)
def plus_1(x):
    return x + 1


@repeat(0)
def mul_2(x):
    return x * 2

print(plus_1(3))  
print(mul_2(4))  
