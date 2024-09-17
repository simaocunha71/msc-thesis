def count_element_in_list(lst: list, el: int) -> int:
  count = 0
  for sub in lst:
    if el in sub:
      count += 1
  return count