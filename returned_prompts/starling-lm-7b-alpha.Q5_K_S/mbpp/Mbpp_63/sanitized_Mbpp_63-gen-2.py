def max_difference(tuples):
    max_diff = 0
    for t in tuples:
        if t[0] < t[1] and t[1] - t[0] > max_diff:
            max_diff = t[1] - t[0]
    return max_diff