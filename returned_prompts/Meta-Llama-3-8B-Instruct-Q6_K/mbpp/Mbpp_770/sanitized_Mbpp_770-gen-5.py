def odd_num_sum(n):
    return sum(i ** 4 for i in range(1, 2 * n + 1, 2))  # 1, 3, 5, ... up to 2n + 1