def count_element_in_list(lst: list, el: int) -> int:
  return sum(el in sublist for sublist in lst)