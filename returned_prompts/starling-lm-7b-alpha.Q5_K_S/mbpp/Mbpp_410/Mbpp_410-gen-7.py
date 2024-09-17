
def min_val(lst: list):
  return min(lst, key=lambda x: isinstance(x, int) + (not x))


