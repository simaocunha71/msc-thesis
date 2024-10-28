
def get_equal(my_tuple):
  length = len(my_tuple[0])
  for i in my_tuple:
    if len(i) != length:
      return False
  return True


