def is_Sub_Array(test_list1: list, test_list2: list) -> bool:
  return all(i in test_list1 for i in test_list2)

