
def cummulative_sum(tuple_list):
  cumsum = 0
  for t in tuple_list:
    for element in t:
      cumsum += element
  return cumsum


