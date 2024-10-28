def count_same_pair(list1: list, list2: list) -> int:
  same_value_indices = [i for i in range(len(list1)) if list1[i] == list2[i]]
  return len(same_value_indices)


