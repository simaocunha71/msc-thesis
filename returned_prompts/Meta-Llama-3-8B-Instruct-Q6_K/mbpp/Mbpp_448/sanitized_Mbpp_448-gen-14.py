def cal_sum(n):
    if n <= 2:
        return 3
    p = [3, 0, 2]
    for _ in range(3, n):
        p.append(p[-1] + p[-2] + p[-3])
    return sum(p[:n])