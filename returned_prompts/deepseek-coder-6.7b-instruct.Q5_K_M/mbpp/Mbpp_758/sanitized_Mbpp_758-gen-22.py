def unique_sublists(lst):
  return {tuple(l): lst.count(l) for l in lst}