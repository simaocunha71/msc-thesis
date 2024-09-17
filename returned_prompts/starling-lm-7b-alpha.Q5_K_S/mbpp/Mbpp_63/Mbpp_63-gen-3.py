
def max_difference(tup_list: list) -> int:
  max_diff = 0
  for tup in tup_list:
    if tup[1] - tup[0] > max_diff:
      max_diff = tup[1] - tup[0]
  return max_diff


