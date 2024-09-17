
from itertools import accumulate
def _sum(iterable, start=0):
    return sum(accumulate(iterable, lambda x, y: x + y))


