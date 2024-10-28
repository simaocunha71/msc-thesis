def odd_num_sum(n):
    total = 0
    num = 1
    for _ in range(n):
        total += num ** 4
        num += 2
    return total