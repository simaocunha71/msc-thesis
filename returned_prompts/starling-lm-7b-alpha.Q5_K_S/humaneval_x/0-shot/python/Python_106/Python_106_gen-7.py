
def f(n):
    l = [0] * n
    for i in range(n):
        if i % 2 == 0:
            l[i] = fact(i)
        else:
            l[i] = sum(range(1, i + 1))
    return l

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def f(n):
    l = [0] * n
    for i in range(n):
        if i % 2 == 0:
            l[i] = fact(i)
        else:
            l[i] = sum(range(1, i + 1))
    return l

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


# Alternative solution
from math import factorial

def f(n):
    l = [0] * n
    for i in range(n):
        if i % 2 == 0:
            l[i] = factorial(i)
        else:
            l[i] = sum(range(1, i + 1))
    return l

from math import factorial

def f(n):
    l = [0] * n
    for i in range(n):
        if i % 2 == 0:
            l[i] = factorial(i)
        else:
            l[i] = sum(range(1, i + 1))
    return l





























































































































