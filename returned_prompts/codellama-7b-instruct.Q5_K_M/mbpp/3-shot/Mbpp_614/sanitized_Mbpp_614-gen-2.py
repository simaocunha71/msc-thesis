def cummulative_sum(tuple_list):
  result = 0
  for t in tuple_list:
    for i in t:
      result += i
  return result