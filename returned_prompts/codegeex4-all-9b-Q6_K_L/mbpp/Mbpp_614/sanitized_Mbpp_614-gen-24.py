def cummulative_sum(tup_list):
  sum = 0
  for tup in tup_list:
    sum += sum(tup)
  return sum