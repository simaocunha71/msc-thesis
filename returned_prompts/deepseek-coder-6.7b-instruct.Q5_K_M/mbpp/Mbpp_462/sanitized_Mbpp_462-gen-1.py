import itertools
from itertools import chain, combinations
from itertools import chain, combinations
def combinations_list(lst):
    result = []
    for i in range(len(lst) + 1):
        for subset in itertools.combinations(lst, i):
            result.append(list(subset))
    return result