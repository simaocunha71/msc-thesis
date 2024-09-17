def cummulative_sum(tuples_list):
    """
    This function will find the cumulative sum of all the values that are present in the given tuple list.
    """
    cumulative_sum = 0
    for t in tuples_list:
        cumulative_sum += sum(t)
    return cumulative_sum