from itertools import zip_longest
from functools import reduce
def tuple_modulo(t1, t2):
    return tuple(reduce(lambda acc, pair: acc + [(pair[0] % pair[1])], zip_longest(t1, t2)))