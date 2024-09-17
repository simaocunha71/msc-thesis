
def count_element_in_list(lst: list,e: int) -> int:
  return sum(1 for sub in lst for i in sub if i == e)


