def cal_sum(n):
    if n < 1:
        return 0
    a, b = 3, 2
    total = 2
    for _ in range(2, n):
        a, b = b, a + b
        total += b
    return total