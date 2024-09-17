def multiply_elements(my_tuple):
  return tuple(i * j for i, j in zip(my_tuple, my_tuple[1:]))