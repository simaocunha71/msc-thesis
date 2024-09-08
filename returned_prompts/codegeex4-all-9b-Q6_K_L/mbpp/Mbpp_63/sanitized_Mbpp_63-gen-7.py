def max_difference(tuples):
    min_val = float('inf')
    max_diff = 0
    for val1, val2 in tuples:
        if val1 < min_val:
            min_val = val1
        if val2 > max_val:
            max_val = val2
        max_diff = max(max_diff, max_val - min_val)
    return max_diff