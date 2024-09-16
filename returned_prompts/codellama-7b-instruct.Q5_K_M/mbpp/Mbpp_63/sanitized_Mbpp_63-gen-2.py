def max_difference(pairs):
    return max(pairs, key=lambda x: x[1])[1] - min(pairs, key=lambda x: x[0])[0]