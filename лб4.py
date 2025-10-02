import math


def f(x):
    return math.sin(x + math.pi / 3) ** 2 - (x**2 / 4) + x


# Вхідні дані
a: float = 0.88
b: float = 0.98
eps: float = 0.005
x0: float = 0.88
n: int = 0

xn: float = f(x0)

while abs(xn - x0) > eps and n < 13:  # максимум 13 ітерацій
    n += 1
    print(f"n{n} = {n}; x{n} = {xn:.6f}; x0{n-1} = {x0:.6f}")
    # Оновлюємо значення для наступної ітерації
    x0 = xn
    xn = f(x0)
