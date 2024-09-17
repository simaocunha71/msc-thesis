def count_element_in_list(lst: list, num: int) -> int:
  return sum(1 for sublist in lst if num in sublist)

