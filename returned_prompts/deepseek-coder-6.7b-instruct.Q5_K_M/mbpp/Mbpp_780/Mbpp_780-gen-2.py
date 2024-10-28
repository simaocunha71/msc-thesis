
from itertools import combinations
def find_combinations(lst):
  return [(sum(x), sum(y)) for x, y in combinations(lst, 2)]


