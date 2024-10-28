def cummulative_sum(tup_list: list) -> int:
  total = 0
  for tup in tup_list:
    total += sum(tup)
  return total