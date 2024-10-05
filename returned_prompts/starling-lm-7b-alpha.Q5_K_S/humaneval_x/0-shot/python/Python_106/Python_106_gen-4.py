
def f(n):
    res = [0] * n
    for i in range(n):
        if i % 2 == 0:
            res[i] = factorial(i)
        else:
            res[i] = sum_nums(i)
    return res

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sum_nums(n):
    if n == 0:
        return 0
    else:
        return sum_nums(n - 1) + n

# Tests
assert f(5) == [1, 2, 6, 24, 15]
assert f(0) == []
assert f(1) == [1]
assert f(2) == [2, 1]
assert f(3) == [6, 2, 1]
assert f(4) == [24, 6, 4, 1]
assert f(5) == [120, 24, 15, 10, 1]
assert f(6) == [720, 120, 60, 20, 10, 1]




def f(n):
    res = [0] * n
    for i in range(n):
        if i % 2 == 0:
            res[i] = factorial(i)
        else:
            res[i] = sum_nums(i)
    return res

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sum_nums(n):
    if n == 0:
        return 0
    else:
        return sum_nums(n - 1) + n

# Tests
assert f(5) == [1, 2, 6, 24, 15]
assert f(0) == []
assert f(1) == [1]
assert f(2) == [2,