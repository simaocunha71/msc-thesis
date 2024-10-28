def odd_position(my_list):
  for index, value in enumerate(my_list):
    if index % 2 != 0 and value % 2 != 0:
      continue
    else:
      return False
  return True