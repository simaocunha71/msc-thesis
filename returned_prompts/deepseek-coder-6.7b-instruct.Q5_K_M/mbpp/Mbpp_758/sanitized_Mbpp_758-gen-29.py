def unique_sublists(lst):
  return {tuple(i): lst.count(i) for i in lst}