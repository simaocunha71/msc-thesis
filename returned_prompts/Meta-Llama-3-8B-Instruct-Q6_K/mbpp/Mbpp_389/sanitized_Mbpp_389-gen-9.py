def find_lucas(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        a, b = 2, 1
        for i in range(3, n+1):
            a, b = b, a+b
        return b