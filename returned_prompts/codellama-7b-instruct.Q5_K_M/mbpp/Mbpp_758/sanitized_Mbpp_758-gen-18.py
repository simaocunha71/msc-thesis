def unique_sublists(lst):
  return {tuple(slst): lst.count(slst) for slst in set(map(tuple, lst))}