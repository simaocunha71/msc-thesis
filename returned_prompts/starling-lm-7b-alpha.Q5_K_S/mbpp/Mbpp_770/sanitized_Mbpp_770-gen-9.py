def odd_num_sum(n):
    total = 0
    for i in range(1, 2*n, 2):
        total += i**4
    return total