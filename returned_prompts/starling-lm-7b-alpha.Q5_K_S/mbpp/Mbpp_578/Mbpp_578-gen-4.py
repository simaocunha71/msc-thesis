
def interleave_lists(list_one, list_two, list_three):
  return [x for list_ in (list_one, list_two, list_three) for x in list_]


