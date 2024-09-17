def count_samepair(test_list1,test_list2,test_list3):
  count = 0
  for i in range(len(test_list1)):
    if test_list1[i] == test_list2[i] == test_list3[i]:
      count += 1
  return count