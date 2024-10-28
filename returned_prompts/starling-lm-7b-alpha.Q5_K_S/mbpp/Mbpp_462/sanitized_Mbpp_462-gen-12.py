from itertools import chain
def combinations_list(s: list) -> list:
  return list(chain(*(map(lambda x: [x], range(len(s) + 1)))))