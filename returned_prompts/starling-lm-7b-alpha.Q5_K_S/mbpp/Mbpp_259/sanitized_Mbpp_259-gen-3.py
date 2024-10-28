from itertools import chain, starmap
from operator import max_
def maximize_elements(t1, t2):
    return tuple(max_((max(a, b), i) for i, (a, b) in enumerate(zip(t1, t2)))[0] for _ in chain.from_iterable(starmap(zip, zip(t1, t2))))