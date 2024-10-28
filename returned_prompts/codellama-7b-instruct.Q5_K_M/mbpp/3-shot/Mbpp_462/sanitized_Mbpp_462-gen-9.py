def combinations_list(my_list):
  from itertools import combinations
  return [list(combination) for r in range(1, len(my_list)+1) for combination in combinations(my_list, r)]