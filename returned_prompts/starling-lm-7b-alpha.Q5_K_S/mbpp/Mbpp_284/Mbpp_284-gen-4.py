
def check_element(list_var: list, element: str) -> bool:
  for i in list_var:
    if i != element:
      return False
  return True


