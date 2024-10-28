def count_element_in_list(lst: list, ele: int) -> int:
  count = 0
  for sublist in lst:
    if ele in sublist:
      count += 1
  return count