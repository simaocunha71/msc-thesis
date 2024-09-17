def extract_index_list(test_list1,test_list2,test_list3):
  return [test_list1[i] for i in range(len(test_list1)) if test_list1[i] == test_list2[i] == test_list3[i]]