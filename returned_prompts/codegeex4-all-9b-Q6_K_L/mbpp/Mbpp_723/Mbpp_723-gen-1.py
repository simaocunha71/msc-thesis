def count_same_pair(test_list1,test_list2):
  count = 0
  for i in range(len(test_list1)):
    if test_list1[i] == test_list2[i]:
      count+=1
  return count

