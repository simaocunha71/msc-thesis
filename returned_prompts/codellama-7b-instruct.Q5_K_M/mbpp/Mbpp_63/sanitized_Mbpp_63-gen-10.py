def max_difference(pairs):
    pairs.sort()
    max_diff = 0
    for i in range(len(pairs) - 1):
        max_diff = max(max_diff, pairs[i+1][0] - pairs[i][1])
    return max_diff