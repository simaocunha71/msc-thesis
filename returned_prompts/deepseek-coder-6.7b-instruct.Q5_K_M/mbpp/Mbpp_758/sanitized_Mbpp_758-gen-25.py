def unique_sublists(lst):
  lst = [tuple(i) for i in lst]
  return {i: lst.count(i) for i in lst}