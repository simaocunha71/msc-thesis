from itertools import chain
def combinations_list(s: list) -> list:
  return list(chain(*[s[:i+1] for i in range(len(s))]))