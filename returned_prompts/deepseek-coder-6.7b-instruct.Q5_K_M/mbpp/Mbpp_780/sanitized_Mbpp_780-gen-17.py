from itertools import combinations
def find_combinations(lst):
  return [(sum(i), sum(j)) for i, j in combinations(lst, 2)]