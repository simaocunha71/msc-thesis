def max_difference(tuples):
    diffs = [abs(t[0] - t[1]) for t in tuples]
    return max(diffs)