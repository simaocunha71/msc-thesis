def overlapping(list1,list2):
  if any(x in list2 for x in list1):
    return True
  else:
    return False