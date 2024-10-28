def Find_Max(list1: list) -> list:
  max_len = 0
  for item in list1:
    if len(item) > max_len:
      max_len = len(item)
  return max_len