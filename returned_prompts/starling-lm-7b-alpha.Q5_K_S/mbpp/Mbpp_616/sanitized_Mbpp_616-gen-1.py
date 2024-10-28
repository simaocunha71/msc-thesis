from functools import reduce
def tuple_modulo(t1, t2):
    return tuple(reduce(lambda x, y: x % y, map(lambda a, b: a, t1, t2)))