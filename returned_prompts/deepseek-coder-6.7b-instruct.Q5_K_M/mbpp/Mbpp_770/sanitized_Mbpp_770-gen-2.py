def odd_num_sum(n):
    sum = 0
    for i in range(n):
        sum += (2*i + 1)**4
    return sum