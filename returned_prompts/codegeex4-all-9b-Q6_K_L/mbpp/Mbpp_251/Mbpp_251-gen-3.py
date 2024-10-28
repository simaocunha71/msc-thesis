def insert_element(lst: list, elem: str) -> list:
  new_lst = []
  for i in lst:
    new_lst.extend([elem, i])
  return new_lst

