
def cummulative_sum(tuple_list: list) -> int:
  sum = 0
  for i in tuple_list:
    for j in i:
      sum += j
  return sum


