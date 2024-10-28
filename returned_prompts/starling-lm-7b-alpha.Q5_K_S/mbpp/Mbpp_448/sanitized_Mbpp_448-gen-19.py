def cal_sum(n):
    a, b = 0, 1
    s = 0
    for i in range(n + 1):
        s += a
        a, b = b, a + b
    return s