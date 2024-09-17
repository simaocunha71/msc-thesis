
def odd_position(lst):
  return all(elm % 2 == 1 for idx, elm in enumerate(lst) if idx % 2 == 1)


