def count(list_1: list) -> int:
  count_list = 0
  for item in list_1:
    if item == True:
      count_list += 1
  return count_list