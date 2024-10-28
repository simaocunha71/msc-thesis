import itertools as it
def combinations_list(items):
  return list(it.chain.from_iterable(it.combinations(items, r) for r in range(len(items)+1)))