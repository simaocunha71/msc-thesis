def odd_num_sum(n):
    total_sum = 0
    for i in range(1, 2*n, 2):
        total_sum += i ** 4
    return total_sum