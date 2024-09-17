
def max_difference(pairs: list) -> int:
    return max(pairs, key=lambda x: x[1] - x[0])[1] - min(pairs, key=lambda x: x[1] - x[0])[1]


