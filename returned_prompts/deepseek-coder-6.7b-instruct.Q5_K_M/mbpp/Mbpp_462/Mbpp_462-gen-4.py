
import itertools
def combinations_list(lst: list) -> list:
  return list(itertools.chain.from_iterable(itertools.combinations(sorted(lst), r) for r in range(len(lst)+1)))


