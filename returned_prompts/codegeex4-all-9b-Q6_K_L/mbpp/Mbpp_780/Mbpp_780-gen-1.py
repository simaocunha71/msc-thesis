def find_combinations(tup_list):
  combinations = []
  for tup1 in tup_list:
    for tup2 in tup_list:
      if tup1 != tup2:
        sum_tups = tuple(map(sum, zip(tup1, tup2)))
        combinations.append(sum_tups)
  return combinations

