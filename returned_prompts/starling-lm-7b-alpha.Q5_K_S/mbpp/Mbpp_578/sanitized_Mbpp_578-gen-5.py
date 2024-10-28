from itertools import chain
from itertools import zip_longest
def interleave_lists(list_a, list_b, list_c):
    return list(chain.from_iterable(zip(list_a, list_b, list_c)))