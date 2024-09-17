
def interleave_lists(list1, list2, list3):
  return [val for pair in zip(list1, list2, list3) for val in pair]


