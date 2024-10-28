def sum_in_range(l: int, r: int) -> int:
    if l % 2 == 0:
        l += 1
    return (r - l + 1) // 2 * (2 * l + r)