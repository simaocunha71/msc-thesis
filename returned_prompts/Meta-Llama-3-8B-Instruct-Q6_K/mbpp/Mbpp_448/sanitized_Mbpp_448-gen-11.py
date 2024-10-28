def cal_sum(n):
    a, b, c = 3, 2, 1
    total = 0
    for _ in range(n):
        total, a, b = a + b, b, a + b
    return total