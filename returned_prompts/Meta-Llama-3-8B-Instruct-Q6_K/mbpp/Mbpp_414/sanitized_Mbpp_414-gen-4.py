def overlapping(list1, list2):
  return any(i in list2 for i in list1) or any(i in list1 for i in list2)