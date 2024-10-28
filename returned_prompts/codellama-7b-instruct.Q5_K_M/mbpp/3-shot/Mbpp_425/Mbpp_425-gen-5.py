
def count_element_in_list(lst: list, element) -> int:
  count = 0
  for sublist in lst:
    if element in sublist:
      count += 1
  return count


