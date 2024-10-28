def tuple_to_int(tup: tuple) -> int:
  res = 0
  for i in range(len(tup)):
    res += tup[i] * 10 ** i
  return res