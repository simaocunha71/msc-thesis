def count_element_in_list(lst: list,element) -> int:
  return sum(1 for sublist in lst for item in sublist if item == element)