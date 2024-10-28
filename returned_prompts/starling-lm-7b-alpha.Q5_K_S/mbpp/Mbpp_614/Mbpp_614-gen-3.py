
def cummulative_sum(tup_list: list) -> int:
  cummulative_sum = 0
  for tup in tup_list:
    cummulative_sum += sum(tup)
  return cummulative_sum


