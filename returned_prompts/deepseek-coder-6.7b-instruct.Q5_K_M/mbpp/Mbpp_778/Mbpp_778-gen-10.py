
from itertools import groupby
def pack_consecutive_duplicates(lst):
    return [[key]*len(list(group)) for key, group in groupby(lst)]


