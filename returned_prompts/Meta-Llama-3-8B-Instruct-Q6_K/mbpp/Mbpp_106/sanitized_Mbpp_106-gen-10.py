def add_lists(lst, t):
  return t + tuple(lst) if type(t) == tuple else (t,) + tuple(lst) if type(t) == int else None