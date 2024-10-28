def last(lst, elm):
  return len(lst) - 1 - lst[::-1].index(elm)