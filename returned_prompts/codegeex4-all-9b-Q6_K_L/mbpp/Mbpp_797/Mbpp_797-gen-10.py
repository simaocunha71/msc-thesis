def sum_in_range(l: int, r: int) -> int:
    if l < 1 or r < 1:
        return 0
    return sum(i for i in range(l, r+1) if i % 2 != 0)