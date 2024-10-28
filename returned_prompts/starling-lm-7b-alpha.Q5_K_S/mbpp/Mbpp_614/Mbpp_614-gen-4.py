
def cummulative_sum(tuples_list):
  total = 0
  for tup in tuples_list:
    total += sum(tup)
  return total


