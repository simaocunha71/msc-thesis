def get_max_sum(n):
    if n == 1:
        return 1
    max_sum = n
    for i in range(1, 5):
        if n % (i+1) == 0:
            max_sum = max(max_sum, n//(i+1) + get_max_sum(n//(i+1)))
    return max_sum