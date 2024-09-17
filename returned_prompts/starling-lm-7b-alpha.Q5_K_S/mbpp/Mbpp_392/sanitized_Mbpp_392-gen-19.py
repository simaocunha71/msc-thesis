def get_max_sum(n: int):
    if n < 1: return 0
    if n < 60: return n
    return max(n, get_max_sum(n//2) + get_max_sum(n//3) + get_max_sum(n//4) + get_max_sum(n//5))