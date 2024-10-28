def cummulative_sum(tup_list: list) -> int:
  cum_sum = 0
  for tup in tup_list:
    cum_sum += sum(tup)
  return cum_sum