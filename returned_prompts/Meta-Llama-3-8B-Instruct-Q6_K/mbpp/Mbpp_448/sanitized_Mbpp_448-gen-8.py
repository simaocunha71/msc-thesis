def cal_sum(n):
    a, b = 3, 2
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total