def count_same_pair(list1: list, list2: list) -> int:
  same_pair_count = 0
  for i in range(len(list1)):
    if list1[i] == list2[i]:
      same_pair_count += 1
  return same_pair_count