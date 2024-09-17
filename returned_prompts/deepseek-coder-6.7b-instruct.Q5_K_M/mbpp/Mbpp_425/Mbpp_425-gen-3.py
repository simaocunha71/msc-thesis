
def count_element_in_list(lst: list, element) -> int:
  return sum(1 for sublist in lst for el in sublist if el == element)


