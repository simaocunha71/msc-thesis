from itertools import combinations
def combinations_list(my_list):
  return list(combinations(my_list, r=len(my_list)))