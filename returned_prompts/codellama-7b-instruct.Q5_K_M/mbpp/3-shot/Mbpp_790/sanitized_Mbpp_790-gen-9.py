def even_position(my_list):
  for i,x in enumerate(my_list):
    if i % 2 == 0 and x % 2 == 0:
      continue
    else:
      return False
  return True