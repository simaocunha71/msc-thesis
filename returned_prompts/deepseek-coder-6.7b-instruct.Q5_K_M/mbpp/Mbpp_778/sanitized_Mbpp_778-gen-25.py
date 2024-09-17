from itertools import groupby
def pack_consecutive_duplicates(lst):
  return [[x for x in group] for key, group in groupby(lst)]