def check_element(lst: list,element: object) -> bool:
  return all(i == element for i in lst)