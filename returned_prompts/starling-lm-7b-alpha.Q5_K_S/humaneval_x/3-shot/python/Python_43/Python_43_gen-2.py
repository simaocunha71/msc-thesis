    def pairs_sum_to_zero_helper(l, i, s):
        if i >= len(l):
            return False
        if s == 0 and i > 0:
            return True
        return (pairs_sum_to_zero_helper(l, i + 1, s + l[i]) or
                pairs_sum_to_zero_helper(l, i + 1, s - l[i]))
    return pairs_sum_to_zero_helper(l, 0, 0)





def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    s = set()
    for e in l:
        if -e in s:
            return True
        s.add(e)
    return False














































def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_