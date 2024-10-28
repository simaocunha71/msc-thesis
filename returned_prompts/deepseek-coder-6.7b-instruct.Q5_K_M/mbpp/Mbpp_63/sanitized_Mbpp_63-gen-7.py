def max_difference(lst):
    max_diff = 0
    for tup in lst:
        diff = abs(tup[0] - tup[1])
        if diff > max_diff:
            max_diff = diff
    return max_diff