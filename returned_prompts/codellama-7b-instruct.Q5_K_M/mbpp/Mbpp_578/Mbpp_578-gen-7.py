
def interleave_lists(list1: list, list2: list, list3: list) -> list:
  assert len(list1) == len(list2) == len(list3)
  return [i for i in zip(list1, list2, list3)]


