
def cummulative_sum(test_tup_list: list) -> int:
  cummulative_sum = 0
  for tup in test_tup_list:
    cummulative_sum += sum(tup)
  return cummulative_sum


