def cal_sum(n):
    a, b, c = 0, 1, 2
    for _ in range(n):
        a, b, c = b, c, a + b + c
    return c