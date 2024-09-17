def count_element_in_list(lst: list,n: int) -> int:
  return sum(n in sublist for sublist in lst)