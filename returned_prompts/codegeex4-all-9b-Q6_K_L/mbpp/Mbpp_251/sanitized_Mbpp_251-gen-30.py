def insert_element(lst: list, el: str) -> list:
  new_lst = []
  for i in lst:
    new_lst.extend([el, i])
  return new_lst