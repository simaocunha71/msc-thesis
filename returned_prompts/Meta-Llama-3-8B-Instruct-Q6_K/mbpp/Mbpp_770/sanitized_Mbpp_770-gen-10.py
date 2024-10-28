def odd_num_sum(n):
    total_sum = sum(i ** 4 for i in range(1, 2*n+1, 2))
    return total_sum