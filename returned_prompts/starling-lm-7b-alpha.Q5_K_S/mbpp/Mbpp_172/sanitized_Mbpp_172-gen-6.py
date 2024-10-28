from collections import Counter
from typing import List
def count_occurance(s: str) -> int:
    """
    Count the number of occurence of the string 'std' in a given string.
    """
    c = Counter(s)
    return c['std']