def Diff(list1, list2):
  return (list(set(list1) - set(list2)) + list(set(list2) - set(list1)))  # remove duplicates and sort the result
  # return sorted(list(set(list1) - set(list2)) + list(set(list2) - set(list1)))  # remove duplicates and sort the result