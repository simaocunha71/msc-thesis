from itertools import chain, combinations
def combinations_list(s: list) -> list:
  return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))