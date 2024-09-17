def interleave_lists(list1: list, list2: list, list3: list) -> list:
  return [list1[i] + list2[i] + list3[i] for i in range(len(list1))]