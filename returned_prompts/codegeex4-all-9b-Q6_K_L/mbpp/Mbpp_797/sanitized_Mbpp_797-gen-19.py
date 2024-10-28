def sum_in_range(l: int, r: int) -> int:
    return sum(x for x in range(l, r+1) if x % 2 != 0)