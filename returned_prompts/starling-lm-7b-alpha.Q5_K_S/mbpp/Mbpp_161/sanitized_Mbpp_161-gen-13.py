def remove_elements(list1: list, list2: list) -> list:
  for element in list2:
    list1.remove(element)
  return list1