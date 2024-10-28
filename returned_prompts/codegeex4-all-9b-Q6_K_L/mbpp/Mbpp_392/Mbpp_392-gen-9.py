def get_max_sum(n):
    if n == 0:
        return 0
    return max(n, get_max_sum(int(n/2)) + get_max_sum(int(n/3)) + get_max_sum(int(n/4)) + get_max_sum(int(n/5)))

