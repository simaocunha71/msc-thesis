def replace_list(list1, list2):
  list1[-1:] = list2
  return list1
  #or return list1 + list2[-len(list1)+1:]  #This will also work