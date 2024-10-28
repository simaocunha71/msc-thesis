def tuple_to_int(my_tuple):
  result = 0
  for i, n in enumerate(my_tuple):
    result += n * 10 ** i
  return result