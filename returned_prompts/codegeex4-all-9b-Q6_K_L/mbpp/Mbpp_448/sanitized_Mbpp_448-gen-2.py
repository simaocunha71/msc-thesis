def cal_sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b, c = 0, 1, 2
        for _ in range(3, n+1):
            a, b, c = b, c, a + b + c
        return c