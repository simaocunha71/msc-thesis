def get_max_sum(n):
    if n <= 1:
        return n
    max_sum = float('-inf')
    for i in range(2, 6):
        if n % i == 0:
            temp_sum = get_max_sum(n // i)
            max_sum = max(max_sum, temp_sum + n)
    return max_sum