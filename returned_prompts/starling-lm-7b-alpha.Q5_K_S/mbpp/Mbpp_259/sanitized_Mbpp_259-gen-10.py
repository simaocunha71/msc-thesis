from itertools import zip_longest
from operator import itemgetter
def maximize_elements(t1, t2):
    zipped = zip_longest(t1, t2)
    zipped = [(x if x is not None else y) for x, y in zipped]
    return list(map(max, zip(*zipped)))