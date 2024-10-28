
def even_position(lst):
  return all(v % 2 == 0 for v in lst[::2])


