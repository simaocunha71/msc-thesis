def cal_sum(n):
    a = b = 1
    sum = 0
    for i in range(n):
        sum += a
        a, b = b, a+b
    return sum
