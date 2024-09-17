
def check_element(list_items: list, element: object) -> bool:
  if len(list_items) == 0:
    return True
  else:
    if list_items[0] != element:
      return False
    else:
      return check_element(list_items[1:], element)


