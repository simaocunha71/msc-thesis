"""
Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
"""
import functools
from typing import List, Optional

def index_maximum(tuples):
    """
    :param tuples: a tuple of tuples
    """
    return max(list(map(lambda tup: (tup[1], tup[0])), tuples))

def index_minimum(tuples):
    """
    :param tuples: a tuple of tuples
    :return: the first value of the smallest second value in a list of tuples
    """
    return min(list(map(lambda tup: (tup[1], tup[0])), tuples))

@functools.lru_cache(maxsize=None)
def index_minimum2(tuples):
    """
    :param tuples: a tuple of tuples
    :return: the first value of the smallest second value in a list of tuples
    """
    return min(list(map(lambda tup: (tup[1], tup[0])), tuples))
