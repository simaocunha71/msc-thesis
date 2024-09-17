def find_combinations(tup_list: list) -> list:
  combinations = []
  for tup1 in tup_list:
    for tup2 in tup_list:
      if tup1 != tup2:
        sum_tup = (tup1[0] + tup2[0], tup1[1] + tup2[1])
        combinations.append(sum_tup)
  return combinations