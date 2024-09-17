
def cummulative_sum(tup_list: list) -> int:
  cummulative_sums = 0
  for tup in tup_list:
    cummulative_sums += sum(tup)
  return cummulative_sums


