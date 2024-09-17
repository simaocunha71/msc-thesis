def cal_sum(n):
    a, b, c = 0, 1, 1
    sum = 0
    for _ in range(n):
        sum += a
        a, b, c = b, c, a + b + c
    return sum

