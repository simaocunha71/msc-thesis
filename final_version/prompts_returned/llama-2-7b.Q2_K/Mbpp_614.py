"""
Write a function to find the cumulative sum of all the values that are present in the given tuple list.
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
"""

def cummulative_sum(tuples):
    """CummulativeSum
    :param tuples: A tuple
    :return: int
    """
    prev = None
    curr_val = None
    if not isinstance(tuples, tuple):
        return False
    
    res_lst = []

    for val in tuples:
        if prev is None or (curr_val + prev != val):
            curr_val = val
            next_res = curr_val
        
        else:
            next_res += curr_val
    
    res_lst.append(next_res)
    
    return res_lst