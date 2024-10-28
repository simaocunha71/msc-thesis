def max_difference(tuples):
    max_diff = 0
    for t in tuples:
        a = t[0]
        b = t[1]
        diff = max(a, b) - min(a, b)
        max_diff = max(max_diff, diff)
    return max_diff