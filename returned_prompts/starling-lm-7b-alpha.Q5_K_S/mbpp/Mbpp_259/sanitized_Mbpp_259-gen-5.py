from itertools import zip_longest
from operator import itemgetter
import sys
from pprint import pprint
def maximize_elements(t1, t2):
    """
    Return a tuple of tuples where each tuple in the result is formed by taking the maximum of the corresponding tuples in t1 and t2.

    >>> maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
    True
    """
    result = []
    for a, b in zip_longest(t1, t2, fillvalue=(-1, -1)):
        result.append((max(a, b), max(b, a)))
    return tuple(result)