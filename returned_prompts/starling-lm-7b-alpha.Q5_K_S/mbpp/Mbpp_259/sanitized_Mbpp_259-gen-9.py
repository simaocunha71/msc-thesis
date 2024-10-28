from itertools import chain, starmap, zip_longest
from operator import itemgetter
from functools import reduce
def maximize_elements(t1, t2):
    return list(reduce(lambda x, y: starmap(max, zip_longest(x, y, fillvalue=itemgetter(0))),
                       zip(t1, t2)))