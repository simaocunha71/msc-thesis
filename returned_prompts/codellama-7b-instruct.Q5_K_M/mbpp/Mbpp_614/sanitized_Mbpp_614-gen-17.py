def cummulative_sum(tuple_list: list) -> int:
  cummulative_sum = 0
  for num in tuple_list:
    if type(num) == int:
      cummulative_sum += num
    else:
      for num in num:
        cummulative_sum += num
  return cummulative_sum