
import itertools
def combinations_list(lst: list) -> list:
  return list(itertools.chain(*[itertools.combinations(lst, i) for i in range(len(lst) + 1)]))


