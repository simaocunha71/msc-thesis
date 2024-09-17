
def cummulative_sum(tuple_list):
  cummulative_sum = 0
  for t in tuple_list:
    for i in t:
      cummulative_sum += i
  return cummulative_sum


