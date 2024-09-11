from itertools import zip_longest
from operator import itemgetter

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

# Created by: Lakshmanan
# Date: 06/08/2020

import sys
from pprint import pprint

def test_maximize_elements():
    assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
    assert maximize_elements(((1, 4), (2, 4), (3, 4)), ((5, 5), (4, 5), (3, 5))) == ((5, 5), (3, 4), (3, 4))
    assert maximize_elements(((1, 2), (3, 4), (5, 6)), ((1, 3), (4, 5), (7, 8))) == ((1, 3), (4, 5), (5, 8))
    assert maximize_elements(((1, 2), (3, 4), (5, 6)), ((1, 3), (4, 5), (7, 8))) == ((1, 