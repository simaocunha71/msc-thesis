def remove_elements(list1: list,list2: list) -> list:
  for i in list2:
    while i in list1:
      list1.remove(i)
  return list1