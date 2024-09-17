def Diff(list1, list2):
  list_diff = []
  for i in list1:
    if i not in list2:
      list_diff.append(i)
  for i in list2:
    if i not in list1:
      list_diff.append(i)
  return list_diff