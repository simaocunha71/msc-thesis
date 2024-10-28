def max_difference(tuples):
    return max([max(pair) - min(pair) for pair in tuples])