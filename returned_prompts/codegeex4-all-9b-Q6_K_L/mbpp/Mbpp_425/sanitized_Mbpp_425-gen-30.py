def count_element_in_list(lst: list, target: int) -> int:
  count = 0
  for sublist in lst:
    if target in sublist:
      count += 1
  return count