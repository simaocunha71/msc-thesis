def odd_num_sum(n):
    sum = 0
    num = 1
    for _ in range(n):
        sum += num ** 4
        num += 2
    return sum