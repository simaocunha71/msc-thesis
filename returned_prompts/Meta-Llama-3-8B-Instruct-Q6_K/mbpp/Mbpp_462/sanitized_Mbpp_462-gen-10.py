from itertools import combinations
def combinations_list(input_list):
  return list(combinations(input_list, r=len(input_list))) + [list(x) for x in combinations(input_list, r) if len(x) < len(input_list)]