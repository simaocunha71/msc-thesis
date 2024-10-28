def max_difference(tuples):
    max_diff = 0
    for t in tuples:
        diff = abs(t[0] - t[1])
        if diff > max_diff:
            max_diff = diff
    return max_diff