def cal_sum(n):
    if n <= 2:
        return 0
    a, b = 3, 2
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total