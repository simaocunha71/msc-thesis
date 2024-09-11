from functools import cmp_to_key
def sort_sublists(sublists):
  return [sorted(sublist) for sublist in sublists]