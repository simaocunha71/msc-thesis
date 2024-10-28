from itertools import combinations
def combinations_list(my_list):
  return list(combinations(my_list, i) for i in range(len(my_list) + 1))