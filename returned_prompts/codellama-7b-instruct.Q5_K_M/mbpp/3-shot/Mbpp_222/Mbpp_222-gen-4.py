
def check_type(my_tuple: tuple) -> bool:
  return len(set(map(type, my_tuple))) == 1


