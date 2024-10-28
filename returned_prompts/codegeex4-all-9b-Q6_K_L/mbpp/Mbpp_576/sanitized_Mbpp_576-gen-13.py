def is_Sub_Array(test_list1, test_list2):
  if set(test_list1).issubset(set(test_list2)):
    return True
  else:
    return False