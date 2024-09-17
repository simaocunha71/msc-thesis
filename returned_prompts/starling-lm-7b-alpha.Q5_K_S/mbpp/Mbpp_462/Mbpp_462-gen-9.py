
from itertools import chain
def combinations_list(seq, r):
    return list(chain(*[combinations(seq, i) for i in range(r+1)]))


