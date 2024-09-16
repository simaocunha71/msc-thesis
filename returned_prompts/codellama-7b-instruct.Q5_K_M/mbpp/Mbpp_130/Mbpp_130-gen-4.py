"""
from collections import Counter
def max_occurrences(lst):
    c = Counter(lst)
    return max(c, key=c.get)
"""