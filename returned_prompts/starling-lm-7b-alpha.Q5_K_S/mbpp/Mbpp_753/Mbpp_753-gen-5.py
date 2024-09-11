"""
To find minimum k records from a tuple list, you can use the built-in Python function sorted(). This function returns a new sorted list from the items in iterable. If key function is specified, then the iterable’s items are sorted according to the function’s return value. Here is an example of how to use it:

def min_k(list_tuple, k):
    return sorted(list_tuple, key=lambda item: item[1])[:k]

In this function, the key function is a lambda function that returns the second element of a tuple (i.e. the score). This ensures that the tuples are sorted by score.

Then, the function uses list slicing to return the first k tuples from the sorted list.

As an example, if you call min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2), it returns [('Akash', 2), ('Akshat', 4)], which are the two tuples with the smallest scores.
"""

def min_k(list_tuple, k):
    return sorted(list_tuple, key=lambda item: item[1])[:k]

assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]

# Python 3.x
from typing import List, Tuple

def min_k(list_tuple: List[Tuple[str, int]], k: int) -> List[Tuple[str, int]]:
    return sorted(list_tuple, key=lambda item: item[1])[:k]

# Python 2.x
def min_k(list_tuple, k):
    return sorted(list_tuple, key=lambda item: item[1])[:k]

# Python 2.x
def min_k(list_tuple, k):
    return sorted(list_tuple, key=lambda item: item[1])[:k]

# Python 3.x
from