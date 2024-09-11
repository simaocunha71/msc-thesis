def pack_consecutive_duplicates(lst):
    """
    Yield consecutive sublists of consecutive duplicates.
    >>> list(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))
    [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
    """
    prev, count = None, 0
    for x in lst:
        if x == prev:
            count += 1
        else:
            if count > 0:
                yield [prev] * count
            count = 1
        prev = x
    if count > 0:
        yield [prev] * count


# Created by: eppesolom
# License: MIT
# Source: https://stackoverflow.com/a/32982075/8135990

# The above code is a generator function, which means it can only be iterated over once.
# Here's an equivalent function which can be called repeatedly:

def pack_consecutive_duplicates_v2(lst):
    """
    Yield consecutive sublists of consecutive duplicates.
    >>> list(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))
    [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
    """
    prev, count = None, 0
    while True:
        for x in lst:
            if x == prev:
                count += 1
            else:
                if count > 0:
                    yield [prev] *