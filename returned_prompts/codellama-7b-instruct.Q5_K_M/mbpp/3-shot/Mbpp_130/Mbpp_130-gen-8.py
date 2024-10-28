
from collections import Counter
def max_occurrences(lst):
    counter = Counter(lst)
    return counter.most_common()[0][0]


