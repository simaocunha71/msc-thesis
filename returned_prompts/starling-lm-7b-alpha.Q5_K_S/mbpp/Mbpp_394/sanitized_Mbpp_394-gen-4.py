from typing import Tuple
def check_distinct(t: Tuple) -> bool:
    """
    Returns True if the given tuple contains no duplicates, False otherwise.

    >>> check_distinct((1, 4, 5, 6, 1, 4))
    False
    >>> check_distinct((1, 2, 3, 4, 5))
    True
    """
    n = len(t)
    for i in range(n):
        for j in range(i+1, n):
            if t[i] == t[j]:
                return False
    return True