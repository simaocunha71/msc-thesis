
def remove_elements(list1, list2):
  for i in list2:
    if i in list1:
      list1.remove(i)
  return list1


