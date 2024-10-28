
def max_difference(tup_list: list) -> int:
  max_diff = 0
  for tup in tup_list:
    diff = max(tup)-min(tup)
    if diff > max_diff:
      max_diff = diff
  return max_diff


