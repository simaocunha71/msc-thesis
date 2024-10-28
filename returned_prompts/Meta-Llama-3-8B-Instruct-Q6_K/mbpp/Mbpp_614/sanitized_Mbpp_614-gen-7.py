def cummulative_sum(tup_list):
  total_sum = 0
  for tup in tup_list:
    total_sum += sum(tup)
  return total_sum