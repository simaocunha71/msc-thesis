def pair_wise(lst):
    """
    Consecutive pairs of items in a given list.
    """
    pairs = []
    for i in range(len(lst)-1):
        pairs.append((lst[i], lst[i+1]))
    return pairs


pair_wise([1,1,2,3,3,4,4,5])
# [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]


# Using two pointers
def pair_wise(lst):
    """
    Consecutive pairs of items in a given list.
    """
    p1, p2 = 0, 0
    pairs = []
    while p2 < len(lst):
        pairs.append((lst[p1], lst[p2]))
        p1 += 1
        p2 += 1
    return pairs


pair_wise([1,1,2,3,3,4,4,5])
# [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]

# Using zip
def pair_wise(lst):
    """
    Consecutive pairs of items in a given list.
    """
    return zip(lst[:-1], lst[1:])


pair_wise([1,1,2,3,3,4,4,5])
# [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]

# Using itertools.zip_longest
import itertools

def pair_wise(lst):
    """
    Consecutive pairs of items in a given list.
    """
    return list(itertools.zip_longest(lst[:-1], lst[1:]))


pair_wise([1,1,2,3,3,4,4,5])
# [(1, 