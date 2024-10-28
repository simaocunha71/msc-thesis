def cal_sum(n):
    if n < 0:
        return 0
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 3
    a, b = 3, 2
    total = 3
    for _ in range(3, n):
        a, b = b, a + b
        total += b
    return total