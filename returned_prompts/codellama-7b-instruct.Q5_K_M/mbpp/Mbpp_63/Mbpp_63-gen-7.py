
def max_difference(pairs: list) -> int:
    return max(max(pair) - min(pair) for pair in pairs)


