
def count_same_pair(test_list1,test_list2):
  return sum(1 for a, b in zip(test_list1, test_list2) if a == b)


