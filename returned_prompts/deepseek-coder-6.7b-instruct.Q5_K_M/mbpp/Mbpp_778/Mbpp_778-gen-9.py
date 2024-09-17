
from itertools import groupby
def pack_consecutive_duplicates(lst):
  return [list(g) for k, g in groupby(lst)]


