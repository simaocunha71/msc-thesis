def lucas_nums(n):
    a, b = 1, 1
    while n:
        a, b = b, a + b
        n -= 1
    return a
def find_lucas(n):
    return lucas_nums(n)