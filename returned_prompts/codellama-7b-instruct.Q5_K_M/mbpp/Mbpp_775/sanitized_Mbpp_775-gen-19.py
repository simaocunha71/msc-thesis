def odd_position(my_list):
  for i in range(len(my_list)):
    if i % 2 != 0 and my_list[i] % 2 != 0:
      return True
  return False