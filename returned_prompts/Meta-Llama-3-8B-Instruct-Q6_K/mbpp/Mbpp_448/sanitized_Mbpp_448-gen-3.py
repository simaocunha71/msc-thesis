def cal_sum(n):
    if n <= 2:
        return 0
    p1, p2 = 3, 2
    total = 0
    for _ in range(2, n):
        p1, p2 = p2, p1 + p2
        total += p2
    return total