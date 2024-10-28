from itertools import combinations
from itertools import combinations
from itertools import combinations
def combinations_list(lst):
    if len(lst) == 0:
        return [[]]
    result = []
    for i in range(len(lst)):
        rest = lst[:i] + lst[i+1:]
        for p in combinations_list(rest):
            result.append([lst[i]] + p)
    return result