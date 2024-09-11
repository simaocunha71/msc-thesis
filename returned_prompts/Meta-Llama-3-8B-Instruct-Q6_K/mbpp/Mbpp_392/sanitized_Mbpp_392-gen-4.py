def get_max_sum(n):
    max_sum = 0
    while n > 4:
        max_sum = max(max_sum, get_max_sum(int(n/2)) + get_max_sum(int(n/3)) + get_max_sum(int(n/4)) + get_max_sum(int(n/5)))
        n = max(int(n/2), int(n/3), int(n/4), int(n/5))
    return max_sum + n