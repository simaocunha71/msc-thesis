import itertools as it
def combinations_list(lst):
  return list(it.chain.from_iterable(it.combinations(lst, r) for r in range(len(lst)+1)))