from itertools import chain, combinations
def combinations_list(lst: list) -> list:
  return list(chain(*[combinations(lst, i) for i in range(len(lst)+1)]))