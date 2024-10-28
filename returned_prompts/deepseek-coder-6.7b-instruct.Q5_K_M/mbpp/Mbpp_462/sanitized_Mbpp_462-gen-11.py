from itertools import chain, combinations
def combinations_list(lst):
  return list(chain(*[combinations(lst, i) for i in range(len(lst)+1)]))