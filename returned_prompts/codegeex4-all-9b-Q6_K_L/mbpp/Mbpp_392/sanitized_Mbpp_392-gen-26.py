def get_max_sum(n: int) -> int:
    return n if n < 3 else max(n, get_max_sum(n // 2) + get_max_sum(n // 3) + get_max_sum(n // 4) + get_max_sum(n // 5))