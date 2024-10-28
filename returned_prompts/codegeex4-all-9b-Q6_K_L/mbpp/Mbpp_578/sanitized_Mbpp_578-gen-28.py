def interleave_lists(list1: list, list2: list, list3: list) -> list:
  return [i for sub_list in zip(list1, list2, list3) for i in sub_list]