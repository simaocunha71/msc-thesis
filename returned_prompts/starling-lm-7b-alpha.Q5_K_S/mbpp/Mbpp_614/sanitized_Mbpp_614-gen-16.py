def cummulative_sum(tuple_list):
  result = 0
  for tup in tuple_list:
    result += sum(tup)
  return result