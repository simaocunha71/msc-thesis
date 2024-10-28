def cal_sum(n):
    a, b, c = 3, 2, 1
    total = 0
    for _ in range(n):
        total += a
        a, b, c = b, c, a + b
    return total