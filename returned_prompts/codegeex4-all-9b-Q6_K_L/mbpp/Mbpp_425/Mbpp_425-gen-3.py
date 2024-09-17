def count_element_in_list(lst: list, num: int) -> int:
  count = 0
  for sublist in lst:
    if num in sublist:
      count += 1
  return count