def max_difference(tuples):
    max_diff = 0
    for t in tuples:
        diff = t[0] - t[1]
        if max_diff < diff:
            max_diff = diff
    return max_diff