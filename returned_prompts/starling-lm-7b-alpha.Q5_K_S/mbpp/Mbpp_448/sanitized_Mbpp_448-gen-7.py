def cal_sum(n):
    p = [0, 1]
    for i in range(2, n + 1):
        p.append(p[i - 1] + p[i - 2] + i ** 3)
    return sum(p)