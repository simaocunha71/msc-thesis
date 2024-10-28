def get_max_sum(n):
    if n % 5 == 0:
        return get_max_sum(n // 5) + n
    if n % 4 == 0:
        return get_max_sum(n // 4) + n
    if n % 3 == 0:
        return get_max_sum(n // 3) + n
    if n % 2 == 0:
        return get_max_sum(n // 2) + n
    return n