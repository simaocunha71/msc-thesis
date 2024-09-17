def unique_sublists(lst):
  return {tuple(sublist): lst.count(sublist) for sublist in lst}

