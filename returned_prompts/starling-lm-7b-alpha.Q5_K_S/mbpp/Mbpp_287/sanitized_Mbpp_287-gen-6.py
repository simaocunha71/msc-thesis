def square_Sum(n):
    res = 0
    for i in range(1, n + 1):
        res += i ** 2
    return res