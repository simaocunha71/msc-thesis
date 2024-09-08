def max_difference(pairs):
    min_val = min(pairs, key=lambda x: x[1])[1]
    max_diff = 0
    for pair in pairs:
        max_diff = max(max_diff, pair[1] - min_val)
        min_val = min(min_val, pair[1])
    return max_diff