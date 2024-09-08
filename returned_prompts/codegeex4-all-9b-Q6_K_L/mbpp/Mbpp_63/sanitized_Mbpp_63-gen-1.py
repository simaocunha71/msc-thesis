def max_difference(pairs):
    min_pair = min(pairs, key=lambda p: p[0])
    max_pair = max(pairs, key=lambda p: p[1])
    return max_pair[1] - min_pair[0]