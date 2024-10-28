from itertools import groupby
from random import randint
from time import time
def pack_consecutive_duplicates(l):
    result = []
    for k, g in groupby(l):
        result.append(list(g))
    return result