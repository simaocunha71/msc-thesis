def count_same_pair(list1,list2):
  same_pairs = 0
  for i in range(len(list1)):
    if list1[i] == list2[i]:
      same_pairs += 1
  return same_pairs