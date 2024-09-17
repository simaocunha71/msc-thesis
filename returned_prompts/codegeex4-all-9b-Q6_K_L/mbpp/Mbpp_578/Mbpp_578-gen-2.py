def interleave_lists(list1, list2, list3):
  return [a for sublist in zip(list1, list2, list3) for a in sublist]

