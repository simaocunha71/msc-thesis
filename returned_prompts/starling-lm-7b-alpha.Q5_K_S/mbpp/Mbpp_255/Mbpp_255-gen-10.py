
from itertools import chain, combinations
def combinations_colors(colors:list,n:int)->list:
  return list(chain(*[combinations(colors,n) for _ in range(len(colors))]))


