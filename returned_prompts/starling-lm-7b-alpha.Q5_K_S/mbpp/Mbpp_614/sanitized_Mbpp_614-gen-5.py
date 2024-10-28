def cummulative_sum(tuples):
    '''
    Find the cumulative sum of all the values that are present in the given tuple list.
    '''
    result = 0
    for tup in tuples:
        result += sum(tup)
    return result