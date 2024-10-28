
def get_max_sum(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return max(n, get_max_sum(n // 2) + get_max_sum(n // 3) + get_max_sum(n // 4) + get_max_sum(n // 5))


