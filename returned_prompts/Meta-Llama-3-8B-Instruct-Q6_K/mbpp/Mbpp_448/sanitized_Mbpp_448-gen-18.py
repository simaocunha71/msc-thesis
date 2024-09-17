def cal_sum(n):
    a, b, c = 3, 2, 0
    total = 0
    for _ in range(n):
        a, b, c = b, c, a + b
        if c <= n:
            total += c
    return total