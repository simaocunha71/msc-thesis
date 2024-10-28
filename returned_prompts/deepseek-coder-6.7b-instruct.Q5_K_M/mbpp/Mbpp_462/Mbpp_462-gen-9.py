
import itertools
def combinations_list(lst):
    return list(itertools.chain.from_iterable(itertools.combinations(lst, r) for r in range(len(lst)+1)))


