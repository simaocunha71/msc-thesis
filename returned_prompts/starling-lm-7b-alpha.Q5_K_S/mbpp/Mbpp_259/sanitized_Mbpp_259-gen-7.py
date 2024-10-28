from itertools import chain, repeat, starmap
from operator import itemgetter
def maximize_elements(tuples1, tuples2):
    return [max(a, b) for a, b in zip(chain(*tuples1), chain(*tuples2))]