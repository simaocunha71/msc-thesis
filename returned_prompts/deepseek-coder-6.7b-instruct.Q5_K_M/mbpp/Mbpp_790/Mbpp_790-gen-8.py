
def even_position(lst):
  return all(el % 2 == 0 for el in lst[::2])


