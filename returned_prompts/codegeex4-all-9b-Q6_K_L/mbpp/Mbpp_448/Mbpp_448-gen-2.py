def cal_sum(n):
    a, b, c = 0, 1, 2
    sum = b
    for i in range(3, n+1):
        a, b, c = b, c, a+b+c
        sum += c
    return sum

