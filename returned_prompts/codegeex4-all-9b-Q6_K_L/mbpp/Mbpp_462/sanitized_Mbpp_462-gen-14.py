def combinations_list(lst):
  from itertools import chain, combinations
  return list(chain(*[combinations(lst, r) for r in range(len(lst)+1)]))