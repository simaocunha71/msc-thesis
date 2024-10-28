def max_difference(pairs):
    """
    Finds the maximum difference between available pairs in the given tuple list.
    :param pairs: List of tuples
    :return: Maximum difference between available pairs
    """
    min_val = float('inf')
    max_diff = 0
    for pair in pairs:
        if pair[0] < min_val:
            min_val = pair[0]
        if pair[1] - pair[0] > max_diff:
            max_diff = pair[1] - pair[0]
    return max_diff