import itertools
def pair_wise(lst):
    """
    Consecutive pairs of items in a given list.
    """
    pairs = []
    for i in range(len(lst)-1):
        pairs.append((lst[i], lst[i+1]))
    return pairs