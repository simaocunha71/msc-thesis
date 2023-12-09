

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    
    if len(l) < 3:
        return False
        
    c = lambda a, b : a + b > 0 and a + b in l
    for i, val in enumerate(l):
        # print(i, val)
        sum_to_zero = any([c(c1, c2) or (c1 == c2) for c1, c2 in triples_within(l, [val])])
        
    if len(l) < 3:
        return False
    
    return sum_to_zero and any([c1 + c2 >= 0 for c1, c2 in triples_within(l, [i])])

def triples_within(a: list, b: list):
    """
    triples_sum_to_zerotakes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_within([1, 3, -2, 1], [0])
    [(-2, 0, 0)]
    """
    
    if not any(triple in a for triple in b):
        return []

    # print(tuple(sorted(set(a), set(b))))
    # sort and eliminate duplicates
    s1