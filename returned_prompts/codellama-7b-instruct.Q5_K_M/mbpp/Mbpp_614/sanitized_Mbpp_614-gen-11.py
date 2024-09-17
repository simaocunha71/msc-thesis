def cummulative_sum(tuple_list: list) -> int:
  cummulative_sum = 0
  for t in tuple_list:
    for elem in t:
      cummulative_sum += elem
  return cummulative_sum