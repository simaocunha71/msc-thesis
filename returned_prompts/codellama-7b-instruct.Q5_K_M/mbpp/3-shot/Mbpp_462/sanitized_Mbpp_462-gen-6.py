import itertools
def combinations_list(input_list: list) -> list:
  combinations_list = list(itertools.combinations(input_list, r=0))
  for i in range(1,len(input_list)+1):
    combinations_list.extend(list(itertools.combinations(input_list, r=i)))
  return combinations_list