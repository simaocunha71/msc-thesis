def add_lists(lst, tup):
  new_lst = list(tup)
  new_lst.extend(lst)
  return tuple(new_lst)