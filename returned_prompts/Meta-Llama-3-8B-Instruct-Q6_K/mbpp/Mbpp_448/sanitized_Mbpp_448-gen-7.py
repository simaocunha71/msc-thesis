def cal_sum(n):
    if n < 3:
        return 0
    a, b = 0, 3
    total = 3
    for _ in range(2, n):
        a, b = b, a + b
        total += b
    return total