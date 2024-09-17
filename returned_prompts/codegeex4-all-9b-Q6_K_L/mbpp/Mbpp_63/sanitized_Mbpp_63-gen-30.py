def max_difference(tuples: list) -> int:
    return max(b - a for a, b in tuples)