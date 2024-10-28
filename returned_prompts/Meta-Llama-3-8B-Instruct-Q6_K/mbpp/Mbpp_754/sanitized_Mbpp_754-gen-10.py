def extract_index_list(list1, list2, list3):
  return list(set([x for x in list1 if x in list2 and x in list3]))