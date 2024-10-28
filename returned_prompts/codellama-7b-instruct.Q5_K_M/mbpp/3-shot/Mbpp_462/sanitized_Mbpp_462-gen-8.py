from itertools import combinations
def combinations_list(my_list):
  return [list(combination) for r in range(1, len(my_list)+1) for combination in combinations(my_list, r)]