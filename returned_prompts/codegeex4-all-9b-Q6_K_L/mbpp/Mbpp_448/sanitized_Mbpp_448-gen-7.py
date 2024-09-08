def cal_sum(n):
    a, b, c = 0, 1, 2
    if n == 1:
        return a
    elif n == 2:
        return b
    elif n == 3:
        return c
    else:
        for i in range(3, n+1):
            a, b, c = b, c, a + b + c
        return c