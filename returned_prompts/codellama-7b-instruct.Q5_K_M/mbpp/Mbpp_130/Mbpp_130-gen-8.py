"""
from collections import Counter
def max_occurrences(my_list):
    counter = Counter(my_list)
    return max(counter, key=counter.get)
"""
