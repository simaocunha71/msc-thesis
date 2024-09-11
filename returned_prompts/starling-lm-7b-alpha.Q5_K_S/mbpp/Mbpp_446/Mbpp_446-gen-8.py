"""
from functools import reduce
from operator import itemgetter
def count_Occurrence(t,l):
    return reduce(itemgetter(1), (i